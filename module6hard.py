class Figure:

    sides_count = 0
    filled = bool

    def __init__(self, __color=[0, 0, 0], __sides=int):
        self.__color = __color
        self.__sides = __sides


    def get_color(self):

        return list(self.__color)

    def _is_valid_color(self, r, g, b):
        colors = [r, g, b]
        valid = 0
        for i in colors:
            if i > 0 and i < 255:
                valid += 1
                if valid == 3:
                    self.__color = colors
                    #print(__color)
            # else:
            #     print(f'Color Error {i}')
        return self.__color

    def set_color(self, r, g, b):
        self._is_valid_color(r, g, b)
        return self.__color


class Circle(Figure):

    sides_count = 1
    __radius = int
    get_square = int


class Triangle(Figure):

    sides_count = 3
    get_square = int


class Cube(Figure):
    # def __init__(self):
    #     super().__init__()

    sides_count = 12
    sides = []
    for i in range(sides_count):
        sides.append(i)
    __sides = sides
    get_volume = int        # обьем куба


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
#print(circle1.get_color())
cube1 = Cube((222, 35, 130), 6)
#print(cube1.get_color())

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())