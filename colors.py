import random

# словарь цветов
colors = {"black": (0,0,0), 
          "red" : (255,0,0),
          "green" : (0,255,0),
          "blue" : (0,0,255),
          "white": (255,255,255)
          }

# Функция определения рандомного цвета из словаря
def random_color():
    color = list(colors.values())
    random_color = random.choice(color)
    return random_color