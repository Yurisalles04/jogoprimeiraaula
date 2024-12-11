import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import C_RED, C_YELLOW, GAME_OVER_POS, MENU_OPTION, MENU_OPTION_GAMEOVER, C_WHITE


class GameOver:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/GameOver.png').convert_alpha()  # Reuse the same background as the score screen
        self.rect = self.surf.get_rect(left=0, top=0)

    def show_game_over(self):  # Renomeado de 'show' para 'show_game_over'
        pygame.mixer_music.load('./assets/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)

        game_over = True
        menu_option = 0  # Starting option (0 for Restart, 1 for Exit)

        while game_over:
            self.score_text(48, 'GAME OVER', C_RED, GAME_OVER_POS['Title'])  # Display Game Over message

            # Display menu options: Restart and Exit
            for i, option in enumerate([MENU_OPTION_GAMEOVER[0], MENU_OPTION_GAMEOVER[1]]):  # Restart and Exit
                color = C_YELLOW if i == menu_option else C_WHITE
                self.score_text(36, option, color, (GAME_OVER_POS['OptionX'], GAME_OVER_POS['OptionY'] + (i * 50)))

            pygame.display.flip()

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Down key to select the next option
                        if menu_option < 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:  # Up key to select the previous option
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = 1

                    if event.key == pygame.K_RETURN:  # Enter key to confirm the option
                        if menu_option == 0:  # Restart the game
                            return 'Restart'
                        elif menu_option == 1:  # Exit the game
                            pygame.quit()
                            quit()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
