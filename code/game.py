#!/usr/bin/python
# -*- coding: utf-8 -*-
from msilib.schema import Font

import pygame
from pygame import Surface, Rect

from code.Const import WIN_WIDHT, WINDOW_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        print('Setup start')
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WINDOW_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
