class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = int
        if self.number_of_floors < new_floor or new_floor < 1:
            print(f'Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print( i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        if isinstance(other, int):
            other += self.number_of_floors
            self.number_of_floors = other
        return self




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

