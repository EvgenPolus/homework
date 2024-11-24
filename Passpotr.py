from string import ascii_letters

class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()


    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        # self.verify_old(old)
        # self.verify_ps(ps)
        # self.verify_weight(weight)

        self.__fio = fio.split()
        # self.__old = old
        # self.__passport = ps
        # self.__weight = weight
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Не верный формат ФИО")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотябы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError(" В ФИО можно использовать только буквенные символы и дефис")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old >120:
            raise TypeError("Возраст должен быть целым числом в диапазоне [14 ; 120]")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Вес должен быть вкщественным числом от 20 и выше")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")
        s = ps.split()                   # Метод Split() используют для разделения строки на несколько частей.
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Не верный формат паспорта")
        for p in s:
            if not p.isdigit():          # Метод isdigit() в Python проверяет, состоит ли строка только из цифр.
                raise TypeError("Серия паспорта должна быть числами")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps

p = Person('Иванов Иван Иванович', 30, '1234 567890', 85.0)
print(p.fio, p.old, p.passport, p.weight)
p.old = 100
p.passport = '4321 698745'
p.weight = 90.0
print(p.old)
print(p.passport)
print(p.weight)





