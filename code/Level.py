#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL, ENEMY_SPEED_LEVEL_1, ENEMY_SPEED_LEVEL_2, ENEMY_SPEED_LEVEL_3, ENEMY_DAMAGE_LEVEL_1, \
    ENEMY_DAMAGE_LEVEL_2, ENEMY_DAMAGE_LEVEL_3, TIMEOUT_LEVEL_1, TIMEOUT_LEVEL_2, TIMEOUT_LEVEL_3
from code.Enemy import Enemy
from code.EntitiyMediator import EntityMediator
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.GameOver import GameOver  # Importe a classe de Game Over

class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int], level_number: int):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.level_number = level_number  # Número do nível para ajustar a dificuldade
        level_name = self.name.replace(" ", "").capitalize()
        self.entity_list.extend(EntityFactory.get_entity(level_name + 'Bg'))  # Adiciona fundo de nível

        # Cria o Player 1 e define a pontuação
        player1 = EntityFactory.get_entity('Player1')
        player1.score = player_score[0]
        self.entity_list.append(player1)

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:  # Multiplayer
            print("Criando Player 2")  # Confirma a criação do Player 2
            player2 = EntityFactory.get_entity('Player2')
            if player2 is not None:
                print(f"Player 2 criado: {player2}")
                player2.score = player_score[1]
                self.entity_list.append(player2)
            else:
                print("Falha na criação do Player 2")

        # Define o tempo de timeout com base no nível
        self.timeout = self.get_timeout_by_level(level_number)

        # Define os timers de spawn de inimigos e de timeout
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def get_timeout_by_level(self, level_number: int):
        """Define o timeout baseado no nível."""
        if level_number == 1:
            return TIMEOUT_LEVEL_1
        elif level_number == 2:
            return TIMEOUT_LEVEL_2
        elif level_number == 3:
            return TIMEOUT_LEVEL_3

    def get_enemy_attributes(self):
        """Define a velocidade e dano dos inimigos conforme o nível."""
        if self.level_number == 1:
            return ENEMY_SPEED_LEVEL_1, ENEMY_DAMAGE_LEVEL_1
        elif self.level_number == 2:
            return ENEMY_SPEED_LEVEL_2, ENEMY_DAMAGE_LEVEL_2
        elif self.level_number == 3:
            return ENEMY_SPEED_LEVEL_3, ENEMY_DAMAGE_LEVEL_3

    def run(self, player_score: list[int]):
        pygame.mixer_music.load('./assets/Level1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            # Exibe as entidades na tela
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                if ent.name == 'Player1':
                    self.level_text(text_size=14, text=f'Player1 - Health:{ent.health} | Score: {ent.score}',
                                    text_color=C_GREEN,
                                    text_pos=(10, 25))

                if ent.name == 'Player2':
                    self.level_text(text_size=14, text=f'Player2 - Health:{ent.health} | Score: {ent.score}',
                                    text_color=C_CYAN,
                                    text_pos=(10, 45))

            # Verificação de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    enemy_speed, enemy_damage = self.get_enemy_attributes()
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    enemy = EntityFactory.get_entity(choice)
                    enemy.speed = enemy_speed
                    enemy.damage = enemy_damage
                    self.entity_list.append(enemy)

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        # Atualiza a pontuação de ambos os jogadores
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                # Verifica se o jogador ainda está na partida
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:  # Se não encontrar o player na lista, game over
                    self.game_over(player_score)  # Chama a tela de Game Over
                    return False

            self.level_text(text_size=14, text=f'{self.name} - Tempo limite: {self.timeout / 1000:.1f}s',
                            text_color=C_WHITE, text_pos=(10, 5))
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=C_WHITE,
                            text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=C_WHITE,
                            text_pos=(10, WIN_HEIGHT - 20))

            pygame.display.flip()
            EntityMediator.verify_colision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def game_over(self, player_score: list[int]):
        # Instancia a classe de GameOver
        game_over_screen = GameOver(self.window)
        result = game_over_screen.show_game_over()  # Chama a tela de Game Over com o nome correto do metodo

        if result == 'Restart':  # Se o jogador escolher reiniciar
            # Resetar o estado do jogo, incluindo a pontuação dos jogadores
            player_score[0] = 0
            player_score[1] = 0
            return True  # Retorna True para reiniciar o nível ou o jogo

        elif result == 'Exit':  # Se o jogador escolher sair
            pygame.quit()
            sys.exit()
