from code.Const import ENTITIY_SPEED
from code.Entity import Entity


class  EnemyShoot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITIY_SPEED[self.name]