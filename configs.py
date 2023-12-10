
import pygame
# Установка размеров окна
size = width, height = 1000, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Alien Invasion')
FPS = 30 # Ограничиваем кол-во FPS
gui_ofset = 200 # Отступ справа от края для интерфейса

# Мир теперь состоит из клеточек
CELL_SIZE = 20 # Размер клетки изменяя этот параметр меняется масштаб
GRID_SIZE_W = (width - gui_ofset) // CELL_SIZE # Задаем ширину сетки мира (-200 Это отступ для интерфеса)
GRID_SIZE_H = height // CELL_SIZE # Задаем высоту сетки мира 

 
# Кортеж направлений
move_directions = (
    (0, -1),  # Вверх 0
    (1, 0),  # Вправо 1
    (0, 1),  # Вниз 2
    (-1, 0),  # Влево 3
)
#>>>>>>>>>>><<<<<<<<<<<