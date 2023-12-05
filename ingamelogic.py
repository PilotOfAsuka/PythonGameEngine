import configs

# Класс определяющий логику Движка хахах ХД
class InGameLogic:
    def __init__(self,):
        pass
    def move_obj(self, obj):
        dx, dy = 10, 5
        new_x = (obj.coord[0] + dx) % configs.width
        new_y = (obj.coord[1] + dy) % configs.height
        obj.coord[0] = new_x
        obj.coord[1] = new_y