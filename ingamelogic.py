import configs

# Класс определяющий логику Движка хахах ХД
class InGameLogic:
    def __init__(self,):
        pass
    def move_obj(self, obj):
        dx, dy = 1, 1
        new_x = (obj.coord[0] + dx) % configs.GRID_SIZE_W
        new_y = (obj.coord[1] + dy) % configs.GRID_SIZE_H
        obj.coord[0] = new_x
        obj.coord[1] = new_y