
import configs as cfg
import colors as c
import main
import pygame

# Класс Slider
class Slider:
    def __init__(self, x, y, w, h, min_val, max_val):
        self.rect = pygame.Rect(x, y, w, h)
        self.min_val = min_val # Минимальное значение
        self.max_val = max_val # Максимальное значение
        self.val = min_val # Значение слайдера
        self.dragging = False # Нажат или нет
    # Обработка событий слайдера
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, _ = event.pos
                self.val = max(min((mouse_x - self.rect.x) / self.rect.width, 1), 0) * (self.max_val - self.min_val) + self.min_val
    # Отрисовка слайдера
    def draw(self, screen):
        pygame.draw.rect(screen, c.WHITE, self.rect)
        slider_pos = int((self.val - self.min_val) / (self.max_val - self.min_val) * self.rect.width)
        pygame.draw.rect(screen, c.FOOD_COLOR, (self.rect.x + slider_pos - 10, self.rect.y, 20, self.rect.height))
    
gui_ofset_x, gui_ofset_y = 10, 0 # Отступы от края ГУИ  
line_text_ofset = 30 # Высота строки
score = 0

def draw_text(text, var,x, y):
    count_text = main.font.render(text +" "+ str(var), True, c.WHITE)
    cfg.screen.blit(count_text, (x,y))

def draw_gui():
    # Отрисовка текста кол-ва клеток
    draw_text("Очки:",score, cfg.width - cfg.gui_ofset + gui_ofset_x , gui_ofset_y + line_text_ofset * 0) # (Текст, Переменная(для счета), х,y)
    draw_text("<Движение>","", cfg.width - cfg.gui_ofset + gui_ofset_x , gui_ofset_y + line_text_ofset * 20)
