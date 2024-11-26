#!/usr/bin/python
# -*- coding: utf-8 -*-
from msilib.schema import Font

import pygame
from pygame import Surface, Rect

from code.Const import WIN_WIDHT, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:  # imagem
            self.window.blit(source=self.surf, dest=self.rect)
            # Corrigido: uso correto de argumentos sem anotações de tipo
            self.menu_text(
                text_size=50,
                text="Corinthians game",
                text_color=C_ORANGE,  # Corrigido: usa = em vez de :
                text_center_pos=((WIN_WIDHT / 2), 70)  # Corrigido: usa = e adiciona parênteses corretos
            )

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(
                        text_size=20,
                        text=MENU_OPTION[i],
                        text_color=C_YELLOW,  # Corrigido: usa = em vez de :
                        text_center_pos=((WIN_WIDHT / 2), 200 + 25 * i)
                        # Corrigido: usa = e adiciona parênteses corretos
                    )

                else:
                    self.menu_text(
                        text_size=20,
                        text=MENU_OPTION[i],
                        text_color=C_WHITE,  # Corrigido: usa = em vez de :
                        text_center_pos=((WIN_WIDHT / 2), 200 + 25 * i)
                        # Corrigido: usa = e adiciona parênteses corretos
                    )
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Fecha a janela
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # down_key
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:  # up_key
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)