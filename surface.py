import configs as cfg
import ingamelogic as brain

# Класс Surface определяет мир или же поверхноть для отрисовки
class Surface:
    def __init__(self, screen):
        self.screen = screen
        self.logic = brain.InGameLogic()
    # Функция отрисовки ВСЕХ обьектов на Surface
    def draw_objs(self):
        for y in range(cfg.GRID_SIZE_H):
            for x in range(cfg.GRID_SIZE_W):
                obj = cfg.world_grid[y][x]
                if obj is not None:
                    obj.draw_obj(self.screen)
                    