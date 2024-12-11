from random import randint

from code.Background import Background
from code.Const import WIN_WIDHT, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        print(f"Solicitando entidade: {entity_name}")  # Depuração para verificar qual entidade está sendo solicitada

        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(4):  # bgimagesnumber level1
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDHT, 0)))
                print(f"Entidade 'Level1Bg' criada com {len(list_bg)} itens")  # Depuração
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(4):  # bgimagesnumber level2
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDHT, 0)))
                print(f"Entidade 'Level2Bg' criada com {len(list_bg)} itens")  # Depuração
                return list_bg
            case 'Level3Bg':
                list_bg = []
                for i in range(6):  # bgimagesnumber level3
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDHT, 0)))
                print(f"Entidade 'Level3Bg' criada com {len(list_bg)} itens")  # Depuração
                return list_bg

            case 'Player1':
                print(f"Entidade 'Player1' criada na posição {(10, WIN_HEIGHT / 2 - 30)}")  # Depuração
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                print(f"Entidade 'Player2' criada na posição {(10, WIN_HEIGHT / 2 + 30)}")  # Depuração
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                print(f"Entidade 'Enemy1' criada com posição aleatória")  # Depuração
                return Enemy('Enemy1', (WIN_WIDHT + 10, randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                print(f"Entidade 'Enemy2' criada com posição aleatória")  # Depuração
                return Enemy('Enemy2', (WIN_WIDHT + 10, randint(40, WIN_HEIGHT - 40)))
            case _:
                print(f"Entidade não encontrada: {entity_name}")  # Depuração para casos não encontrados
                return None
