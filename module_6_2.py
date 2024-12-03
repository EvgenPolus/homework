class Vehicle:                                                      # это любой транспорт
     owner = str                                                    # владелецтранспорта.(можетменяться)
     __model = str                                                  # модель транспорта.(не можем менять)
     __engine_power = int                                           # мощность двигателя.
     __color = str                                                  # название цвета
     __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # список допустимых цветов

     def get_model(self, __model):
         pass
     def get_horsepower(self, __engine_power):
         pass
     def get_color(self, __color):
         pass
     def print_info():
         print(f'{get_model}, {get_horsepower}, {get_color}, "Владелец: {owner name}"')

     def set_color():
         new_color = str
         if new_color in __COLOR_VARIANTS[]:
            __color = new_color
         else:
             print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5