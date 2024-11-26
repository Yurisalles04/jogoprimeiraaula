#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint  # Corrigido para importar 'randint'

from code.Background import Background
from code.Const import WIN_WIDHT, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDHT, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                # Usando randint para gerar a posição aleatória no intervalo correto
                return Enemy('Enemy1', (WIN_WIDHT + 10, randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDHT + 10, randint(40, WIN_HEIGHT - 40)))


