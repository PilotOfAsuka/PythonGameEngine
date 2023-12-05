import main
import ingamelogic as brain
# Класс Surface определяет мир или же поверхноть для отрисовки
class Surface:
    def __init__(self, screen):
        self.screen = screen
        # Список обьектов \/\/\/\/\/\/\/ Хммм... 
        self.objs = main.objs
        self.logic = brain.InGameLogic()
        
    # Функция отрисовки ВСЕХ обьектов на Surface
    def draw_objs(self):
        for obj in self.objs:
            obj.draw_obj(self.screen)
    def move_objs(self):
        for obj in self.objs:
            self.logic.move_obj(obj)