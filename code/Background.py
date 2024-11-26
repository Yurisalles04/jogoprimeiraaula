#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDHT, ENTITIY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITIY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDHT