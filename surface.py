import configs as cfg
import func
import colors as c
import objects as objs

# Инициализация двумерного массива мира
world_grid = [[None for _ in range(cfg.GRID_SIZE_W)] for _ in range(cfg.GRID_SIZE_H)] # Массив мира
ship = objs.Ship(cfg.GRID_SIZE_W // 2, cfg.GRID_SIZE_H - 5, c.BLACK)
world_grid[ship.x][ship.y] = ship

# Класс Surface определяет мир или же поверхноть для отрисовки
class Surface:
    def __init__(self, surface):
        self.world = surface
        pass
        
    # Функция отрисовки обьектов на Surface
    def draw_objs(self):
        for y in range(cfg.GRID_SIZE_H):
            for x in range(cfg.GRID_SIZE_W):
                obj = world_grid[y][x]
                if isinstance(obj, objs.Ship):
                    func.draw_obj(obj)
                    
