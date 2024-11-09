#!/usr/bin/python
# -*- coding: utf-8 -*-
from msilib.schema import Font

import pygame
from pygame import Surface, Rect

from code.Const import WIN_WIDHT, COLOR_ORANGE, MENU_OPTION, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self):
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            # Corrigido: uso correto de argumentos sem anotações de tipo
            self.menu_text(
                text_size=50,
                text="Corinthians game",
                text_color= COLOR_ORANGE,  # Corrigido: usa = em vez de :
                text_center_pos=((WIN_WIDHT / 2), 70)  # Corrigido: usa = e adiciona parênteses corretos
            )

            for i in range(len(MENU_OPTION)):
                self.menu_text(
                    text_size=20,
                    text=MENU_OPTION[i],
                    text_color=C_WHITE,  # Corrigido: usa = em vez de :
                    text_center_pos=((WIN_WIDHT / 2), 200 + 25 * i)  # Corrigido: usa = e adiciona parênteses corretos
                )

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Fecha a janela
                    pygame.quit()
                    quit()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

