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

    @classmethod
    def __check_dat(cls, other):
        if isinstance(other, House):
            other = other.number_of_floors
        elif isinstance(other, int):
            other = other
        return other

    def __eq__(self, other):
        oth = self.__check_dat(other)
        return self.number_of_floors == oth

    def __add__(self, other):
        oth = self.__check_dat(other)
        self.number_of_floors += oth
        return self

    def __iadd__(self, other):
        oth = self.__check_dat(other)
        self.number_of_floors += oth
        return self

    def __radd__(self, other):
        oth = self.__check_dat(other)
        oth += self.number_of_floors
        self.number_of_floors = oth
        return self

    def __lt__(self, other):
        oth = self.__check_dat(other)
        return self.number_of_floors < oth

    def __gt__(self, other):
        oth = self.__check_dat(other)
        return self.number_of_floors > oth

    def __ge__(self, other):
        oth = self.__check_dat(other)
        return self.number_of_floors >= oth

    def __le__(self, other):
        oth = self.__check_dat(other)
        return self.number_of_floors <= oth

    def __ne__(self, other):
        oth = self.__check_dat(other)
        return self.number_of_floors != oth



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
