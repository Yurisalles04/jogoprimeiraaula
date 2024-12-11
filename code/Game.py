import sys
import pygame
from code.Const import MENU_OPTION, WIN_WIDHT, WIN_HEIGHT
from code.GameOver import GameOver
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        print('Setup start')
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WIN_HEIGHT))
        self.running = True
        self.player_scores = [0, 0]  # Inicializa as pontuações dos jogadores
        self.current_level = 1  # Começa pelo nível 1
        self.game_mode = MENU_OPTION[0]  # Define o modo de jogo (pode ser ajustado conforme o menu)

    def run(self):
        """Inicia o jogo."""
        while self.running:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            # Atualizar game_mode conforme a escolha do menu
            if menu_return == MENU_OPTION[0]:  # Single Player
                self.game_mode = MENU_OPTION[0]
            elif menu_return == MENU_OPTION[1]:  # Multiplayer
                self.game_mode = MENU_OPTION[1]
            elif menu_return == MENU_OPTION[2]:  # Outro modo
                self.game_mode = MENU_OPTION[2]

            # Verifique o valor retornado do menu
            print(f"Menu retornou: {menu_return}")

            # Se o jogador escolher algum dos modos de jogo (Single Player ou Multiplayer)
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                self.player_scores = [0, 0]  # Inicializa a pontuação dos jogadores

                # Executa os níveis sequencialmente
                for level_number in range(1, 4):  # Agora vai de 1 até 3
                    self.run_level(level_number)

                # Se todos os níveis forem completados, salva a pontuação
                score.save(menu_return, self.player_scores)

            # Se o jogador escolher ver o ranking
            elif menu_return == MENU_OPTION[3]:
                score.show()

            # Se o jogador escolher sair do jogo
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Fecha a janela
                quit()

            else:
                pass

    def run_level(self, level_number):
        """Controla a execução de cada nível."""
        print(f"Modo de jogo atual: {self.game_mode}")  # Verifica o valor de game_mode
        level = Level(self.window, f"LEVEL {level_number}", self.game_mode, self.player_scores, level_number)
        level_return = level.run(self.player_scores)

        if not level_return:  # Se retornar False, significa que o jogo acabou (game over)
            self.game_over()

    def game_over(self):
        """Exibe a tela de Game Over."""
        game_over_screen = GameOver(self.window)
        result = game_over_screen.show_game_over()  # Mostra a tela de Game Over

        if result == 'Restart':  # Se o jogador escolher reiniciar
            self.restart_game()  # Reinicia o jogo
        elif result == 'Exit':  # Se o jogador escolher sair
            self.quit_game()  # Sai do jogo

    def restart_game(self):
        """Reinicia o jogo."""
        self.player_scores = [0, 0]  # Reseta as pontuações
        self.current_level = 1  # Reinicia no nível 1
        self.run()  # Recomeça o jogo

    def quit_game(self):
        """Sai do jogo."""
        pygame.quit()
        sys.exit()

