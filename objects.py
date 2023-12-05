import pygame
import ingamelogic as brain
import configs as cfg
# Класс OBJ определяет родительский класс обьектов основные параметры обьекта координаты и к примеру цвет
class OBJ:
    def __init__(self, x, y, color):
        self.color = color # Цвет обьекта
        self.coord = [x,y] # Координаты обьекта
        self.logic = brain.InGameLogic()
        # Нужно дополнить (Физика?)

# Класс Square определяет  дочерний класс обьекта "Квадрат" имеет функцию отрисовки
class Square(OBJ):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    # Функция отрисовки квадрата   
    def draw_obj(self, world):
        param = pygame.Rect(self.coord[0] * cfg.CELL_SIZE ,self.coord[1] * cfg.CELL_SIZE ,cfg.CELL_SIZE, cfg.CELL_SIZE)
        pygame.draw.rect(world, self.color, param) 

#Класс Circle опредделяет дочерний класс обьекта "Круг"
class Circle(OBJ):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    # Функция отрисовки круга   
    def draw_obj(self, world):
        pygame.draw.circle(world,self.color,(self.coord[0] * (cfg.CELL_SIZE) + cfg.CELL_SIZE/2, self.coord[1] * (cfg.CELL_SIZE)+ cfg.CELL_SIZE/2), cfg.CELL_SIZE/2)    