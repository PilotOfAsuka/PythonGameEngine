import pygame
import configs as cfg

# Класс OBJ определяет родительский класс обьектов основные параметры обьекта координаты и к примеру цвет
class OBJ:
    def __init__(self, x, y, color):
        self.color = color # Цвет обьекта
        self.x = x # Координаты обьекта
        self.y = y # Координаты обьекта
        # Нужно дополнить (Физика?)

# Класс Square определяет  дочерний класс обьекта "Квадрат" имеет функцию отрисовки
class Square(OBJ):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


#Класс Circle опредделяет дочерний класс обьекта "Круг"
class Circle(OBJ):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    # Функция отрисовки круга   
    def draw_obj(self, world):
        pygame.draw.circle(world,self.color,(self.coord[0] * (cfg.CELL_SIZE) + cfg.CELL_SIZE/2, self.coord[1] * (cfg.CELL_SIZE)+ cfg.CELL_SIZE/2), cfg.CELL_SIZE/2)   
        
# Класс комплексного обьекта
class ComplexObj:
    def __init__(self, matrix, start_x, start_y, color):
        self.coord = [start_x, start_y]
        self.squares = [] # массив комплексного обьекта
        # Конструктор обьектов
        for y, row in enumerate(matrix):
            square_row = []
            for x, cell in enumerate(row):
                if cell == 1:
                    square = Square(self.coord[0] + x, self.coord[1] + y, color)
                    square_row.append(square)
                else:
                    square_row.append(None)
            self.squares.append(square_row)

class Ship(OBJ):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)     
        self.move_x_left = False
        self.move_x_right = False
        self.move_y_up = False
        self.move_y_down = False
        self.dir_index = 0
        
    def move_obj(self, dir_index):
        dx, dy = cfg.move_directions[dir_index]
        if self.move_x_left == True or self.move_x_right == True:
            new_x = (self.x + dx) % cfg.GRID_SIZE_W
            self.x = new_x
        if self.move_y_up == True or self.move_y_down == True:    
            new_y = (self.y + dy) % cfg.GRID_SIZE_H
            self.y = new_y
