import configs as cfg
import pygame
import surface
import colors
import main
import gui



# Класс Арр определяет окно Pygame и его цикл        
class App:
    def __init__(self):
        self.run = True
        self.screen = cfg.screen
        self.surface = surface.Surface(self.screen)
        self.gui = gui
    # Обработка Евентов Pygame    
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    surface.ship.dir_index = 3
                    surface.ship.move_x_left = True
                                   
                if event.key == pygame.K_RIGHT:
                    surface.ship.dir_index = 1
                    surface.ship.move_x_right = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    surface.ship.move_x_left = False
                if event.key == pygame.K_RIGHT:
                    surface.ship.move_x_right = False
                

    # Активация и отрисовка графической части окна            
    def draw(self):
        self.screen.fill(colors.BKG_COLOR)  
        self.surface.draw_objs()
        
    # Основной цикл       
    def loop(self):
        while self.run:
            self.event()
            surface.ship.move_obj(surface.ship.dir_index)
            self.draw()
            self.gui.draw_gui()
            pygame.display.flip() 
            main.clock.tick(cfg.FPS)# FPS пока так топорно меняем скорость циклов :(
    
