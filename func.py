import random
import configs as cfg
import pygame


#Здесь можно хранить одиночные функции

# Функция для генерации случайной свободной позиции
def random_position(world_grid):
    x = random.randint(0, cfg.GRID_SIZE_W - 1)
    y = random.randint(0, cfg.GRID_SIZE_H - 1)
    while world_grid[y][x] is not None:
        x = random.randint(0, cfg.GRID_SIZE_W - 1)
        y = random.randint(0, cfg.GRID_SIZE_H - 1)
    return x, y #Возврат случайных свободных позиций

                    
# функция получения свободного места вокруг
def get_free_adjacent_positions(position, world_grid):
    x, y = position
    free_positions = []
    for dx, dy in cfg.move_directions:
        nx = x + dx if -1 < x + dx < cfg.GRID_SIZE_W else x
        ny = y + dy if -1 < y + dy < cfg.GRID_SIZE_H else y
        if world_grid[ny][nx] is None:
            free_positions.append((nx, ny))
    return free_positions # Возврат свободных позиций

# Функция отрисовки объектов
def draw_obj(obj):
    x, y = obj.x, obj.y
    rect = pygame.Rect(x * cfg.CELL_SIZE, y * cfg.CELL_SIZE, cfg.CELL_SIZE, cfg.CELL_SIZE)
    pygame.draw.rect(cfg.screen, obj.color, rect)
    
# функция чормализации значения один диапазон в другой (например кол-во потребления энергии от 0 до 200 зависит от температуры, или другого значенмия)
def normalize_value(input_value, original_min, original_max, target_min, target_max):
    
    # Преобразуем исходное значение в диапазоне от 0 до 1
    normalized = (input_value - original_min) / (original_max - original_min)
    # Преобразуем нормализованное значение в целевой диапазон
    return normalized * (target_max - target_min) + target_min

