import configs as cfg

# Класс определяющий логику Движка хахах ХД
class InGameLogic:
    def __init__(self,):
        pass
    def move_obj(self, obj, dir_index):
        dx, dy = cfg.dir[dir_index]
        new_x = (obj.coord[0] + dx) % cfg.GRID_SIZE_W
        new_y = (obj.coord[1] + dy) % cfg.GRID_SIZE_H
        obj.coord[0] = new_x
        obj.coord[1] = new_y