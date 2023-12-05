# ИмПоРтЫ
import pygame
import app
import objects as objs
import colors as c
import func
import configs as cfg

# Инициализация Pygame
pygame.init()
clock = pygame.time.Clock()

# Создаем 10 квадратиков
for _ in range(10):
    x, y = func.random_position(cfg.world_grid)
    obj = objs.Square(x,y, c.random_color())
    cfg.world_grid[y][x] = obj
    
# Создаем 10 кружочков
for _ in range(10):
    x, y = func.random_position(cfg.world_grid)
    obj = objs.Circle(x,y, c.random_color())
    cfg.world_grid[y][x] = obj


# Main.py :D  
if __name__ == "__main__":
    app = app.App()
    app.loop()