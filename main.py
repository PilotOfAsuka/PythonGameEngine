# ИмПоРтЫ
import pygame
import app
import objects as obj
import colors as c
# Инициализация Pygame
pygame.init()

#objs = Sqare(100,100,RED)  
objs = [obj.Square(0,0,c.RED),obj.Square(100,100,c.GREEN),obj.Square(200,200,c.BLUE),obj.Square(100,200,c.RED), obj.Circle(75,75,c.BLUE,50)]
# Main.py :D  
if __name__ == "__main__":
    app = app.App()
    app.loop()