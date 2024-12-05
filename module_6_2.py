class Vehicle:                                                      # это любой транспорт
    def __init__(self, owner, model, color, engine_power):
     self.owner = owner                                             # владелецтранспорта.(можетменяться)
     self.__model = model                                                 # модель транспорта.(не можем менять)
     self.__engine_power = engine_power                                           # мощность двигателя.
     self.__color = color                                                  # название цвета
     __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # список допустимых цветов

     def get_model():
         print(f' "Модель: {self.__model}"')

     def get_horsepower():
         print(f' "Мощность двигателя: {self.__engine_power}"')

     def get_color():
         print(f'"Цвет: {self.__color }')

     def print_info():
         print(f'{get_model()}, {get_horsepower()}, {get_color()}, "Владелец: {owner()}"')

     def set_color(self, new_color):

         if new_color.upper() in __COLOR_VARIANTS.upper():
            __color = new_color
         else:
             print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()