import configs as cfg
import ingamelogic as brain
import main
# Класс Surface определяет мир или же поверхноть для отрисовки
class Surface:
    def __init__(self, screen):
        self.screen = screen
        # Инициализация двумерного массива в самом мире
        self.world_grid = main.world_grid
        self.logic = brain.InGameLogic()
    # Функция отрисовки ВСЕХ обьектов на Surface
    def draw_objs(self):
        for y in range(cfg.GRID_SIZE_H):
            for x in range(cfg.GRID_SIZE_W):
                obj = self.world_grid[y][x]
                if obj is not None:
                    obj.draw_obj(self.screen)
                    self.logic.move_obj(obj)