import configs
import pygame
import surface
import colors
# Класс Арр определяет окно Pygame и его цикл        
class App:
    def __init__(self):
        self.run = True
        self.screen = pygame.display.set_mode(configs.size)
        self.surface = surface.Surface(self.screen)
    # Обработка Евентов Pygame    
    def event(self):
        self.surface.move_objs()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
    # Активация и отрисовка графической части окна            
    def draw(self):
        self.screen.fill(colors.BLACK)  
        self.surface.draw_objs()
    # Основной цикл       
    def loop(self):
        while self.run:
            self.draw()
            self.event()
            pygame.display.flip() # из за этой стройки мучался блин , черный экран был
            pygame.time.delay(100) # ФПС ННАДА!!