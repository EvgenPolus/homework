class Vehicle:                                                      # это любой транспорт
     owner = str                                                    # владелецтранспорта.(можетменяться)
     __model = str                                                  # модель транспорта.(не можем менять)
     __engine_power = int                                           # мощность двигателя.
     __color = str                                                  # название цвета
     __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # список допустимых цветов

     def get_model(self, model):
         self.__model = model

     def get_horsepower(self, engine_power):
         self.__engine_power = engine_power

     def get_color(self, color):
         self.__color = color

     def print_info():
         print(f'{get_model}, {get_horsepower}, {get_color}, "Владелец: {owner}"')

     def set_color(self, new_color):

         if new_color.upper() in __COLOR_VARIANTS.upper():
            __color = new_color
         else:
             print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
