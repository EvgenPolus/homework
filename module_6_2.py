class Vehicle:                                                               # это любой транспорт
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']            # список допустимых цветов
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner                                                   # владелецтранспорта.(можетменяться)
        self.__model = model                                                 # модель транспорта.(не можем менять)
        self.__engine_power = engine_power                                   # мощность двигателя.
        self.__color = color                                                 # название цвета

    def get_model(self):
        print(f' "Модель: {self.__model}"')

    def get_horsepower(self):
        print(f' "Мощность двигателя: {self.__engine_power}"')

    def get_color(self):
        print(f' "Цвет: {self.__color }')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f' "Владелец: {self.owner}"')


    def set_color(self, new_color):
        if new_color.upper() in (a.upper() for a in self.__COLOR_VARIANTS):
           self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()