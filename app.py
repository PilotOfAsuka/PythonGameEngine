import configs as cfg
import pygame
import surface
import colors
import main
import ingamelogic as brain
# Класс Арр определяет окно Pygame и его цикл        
class App:
    def __init__(self):
        self.run = True
        self.screen = pygame.display.set_mode(cfg.size)
        self.surface = surface.Surface(self.screen)
        self.logic = brain.InGameLogic()
        
    # Обработка Евентов Pygame    
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for y in range(cfg.GRID_SIZE_H):
                        for x in range(cfg.GRID_SIZE_W):
                            obj = cfg.world_grid[y][x]
                            if obj is not None:
                                self.logic.move_obj(obj, "left")
                elif event.key == pygame.K_RIGHT:
                    for y in range(cfg.GRID_SIZE_H):
                        for x in range(cfg.GRID_SIZE_W):
                            obj = cfg.world_grid[y][x]
                            if obj is not None:
                                self.logic.move_obj(obj, "right")                    
                elif event.key == pygame.K_UP:
                    for y in range(cfg.GRID_SIZE_H):
                        for x in range(cfg.GRID_SIZE_W):
                            obj = cfg.world_grid[y][x]
                            if obj is not None:
                                self.logic.move_obj(obj, "up")                    
                elif event.key == pygame.K_DOWN:
                    for y in range(cfg.GRID_SIZE_H):
                        for x in range(cfg.GRID_SIZE_W):
                            obj = cfg.world_grid[y][x]
                            if obj is not None:
                                self.logic.move_obj(obj, "down")                    


    # Активация и отрисовка графической части окна            
    def draw(self):
        self.screen.fill(colors.colors["white"])  
        self.surface.draw_objs()
    # Основной цикл       
    def loop(self):
        while self.run:
            self.draw()
            self.event()
            pygame.display.flip() # из за этой стройки мучался блин , черный экран был
            main.clock.tick(cfg.FPS)# ФПС ННАДА!!