import random
import configs as cfg
#Здесь можно хранить одиночные функции

# Функция для генерации случайной свободной позиции
def random_position(world_grid):
    x = random.randint(0, cfg.GRID_SIZE_W - 1)
    y = random.randint(0, cfg.GRID_SIZE_H - 1)
    while world_grid[y][x] is not None:
        x = random.randint(0, cfg.GRID_SIZE_W - 1)
        y = random.randint(0, cfg.GRID_SIZE_H - 1)
    return x, y
# Функция установки обьектов в мире
def place_in_world(world, complex_obj):
    for y, row in enumerate(complex_obj.squares):
        for x, square in enumerate(row):
            if square is not None:
                world_y = complex_obj.coord[1] + y
                world_x = complex_obj.coord[0] + x
                if 0 <= world_x < cfg.GRID_SIZE_W and 0 <= world_y < cfg.GRID_SIZE_H:
                    world[world_y][world_x] = square