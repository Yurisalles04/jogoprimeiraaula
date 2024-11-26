#!/usr/bin/python
# -*- coding: utf-8 -*-
from msilib.schema import Font

import pygame
from pygame import Surface, Rect

from code.Const import WIN_WIDHT, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        print('Setup start')
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'LEVEL 1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit() # CLOSE WINDOW
                quit()
            else:
                pass






