#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.EntitiyMediator import EntityMediator
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):

        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo que vem do menu
        self.entity_list: list[Entity] = []
        level_name = self.name.replace(" ", "").capitalize()  # Remove espaços no nome (ex: 'LEVEL 1' -> 'Level1')
        self.entity_list.extend(EntityFactory.get_entity(level_name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        self.timeout = TIMEOUT_LEVEL  # Exemplo: adicione um valor para timeout
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        # Define o evento de inimigos que ocorre a cada 2000 milissegundos
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # 100milisegundos

    def run(self, player_score: list[int]):
        pygame.mixer_music.load('./assets/Level1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            # Desenha cada entidade e move-a
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()  # Chama o metodo
                    if shoot is not None:
                        self.entity_list.append(shoot)  # Adiciona o objeto PlayerShoot à lista
                if ent.name == 'Player1':
                    self.level_text(text_size=14, text=f'Player1 - Health:{ent.health} | Score: {ent.score}',
                                    text_color=C_GREEN,
                                    text_pos=(10, 25))
                if ent.name == 'Player2':
                    self.level_text(text_size=14, text=f'Player2 - Health:{ent.health} | Score: {ent.score}',
                                    text_color=C_CYAN,
                                    text_pos=(10, 45))

            # Lida com eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Fecha a janela
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:  # Verifica o tipo do evento corretamente
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            # Exibe o texto no jogo
            self.level_text(text_size=14, text=f'{self.name} - Tempo limite: {self.timeout / 1000:.1f}s',
                            text_color=C_WHITE, text_pos=(10, 5))
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=C_WHITE,
                            text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=C_WHITE,
                            text_pos=(10, WIN_HEIGHT - 20))
            # Atualiza a tela
            pygame.display.flip()
            # colision
            EntityMediator.verify_colision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_pos)  # Alinha o texto pelo canto superior esquerdo
        self.window.blit(source=text_surf, dest=text_rect)
