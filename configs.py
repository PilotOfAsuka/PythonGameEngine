# Установка размеров окна
size = width, height = 800, 600
FPS = 20
# Мир теперь состоит из клеточек
CELL_SIZE = 20 # размер клетки изменяя этот параметр меняется масштаб
GRID_SIZE_W = width // CELL_SIZE
GRID_SIZE_H = height // CELL_SIZE

# Инициализация двумерного массива мира
world_grid = [[None for _ in range(GRID_SIZE_W)] for _ in range(GRID_SIZE_H)]

# Словарь направлений
dir = {"up":[0,-1], "down":[0, 1], "left":[-1, 0], "right":[1, 0]}