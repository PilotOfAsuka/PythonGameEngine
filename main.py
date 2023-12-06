# ИмПоРтЫ
import pygame
import app
import objects as objs
import colors as c
import func
import configs as cfg
import obj_matrixs as matx

# Инициализация Pygame
pygame.init()
clock = pygame.time.Clock()

# Создаем комплексный Объект
test_obj = objs.ComplexObj(matx.obj_1,10,10,c.colors["black"])
test_obj1 = objs.ComplexObj(matx.obj_1,0,0,c.colors["red"])

func.place_in_world(cfg.world_grid, test_obj)
func.place_in_world(cfg.world_grid, test_obj1)
# Main.py :D  
if __name__ == "__main__":
    app = app.App()
    app.loop()