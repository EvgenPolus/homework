# "list comprehension"
# Списковые сборки

# встроенные функции высшего порядка: map() и filter()
# Функция map() применяется для преобразования каждого элемента в коллекции
# с помощью заданной функции.
# Функция filter() используется для фильтрации элементов, оставляя только те,
# которые соответствуют заданному условию.

def by_3(x):
    return x * 3

def is_odd(x):
    return x % 2
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = map(by_3, filter(is_odd, my_numbers))
print(list(result))

# пример списковой сборки

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
list_comp_1 = [x*2 for x in my_numbers]
print(list_comp_1)

# пример списковой сборки

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = [x*3 for x in my_numbers]
print(result)


#  в списковой сборке можно также фильтровать данные,
#  комбинируя возможности функций map и filter
# в конце цикла for добавляется условие,
# например, "if x > 5", if type(x) == чему-то", или "if x % 5 == 0".

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
list_comp_1 = [x*2 for x in my_numbers if x > 2 and x % 2 !=0]
print(list_comp_1)

# можно добавлять условие непосредственно после объявления операции
# и элемента в генераторе списка, перед циклом «for»
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
list_comp_3 = [x*2 if x > 2 else x * 10 for x in my_numbers]
print(list_comp_3)

# ПРИМЕР № 4
# условие ставится перед циклом, чтобы не фильтровать данные в исходной коллекции

my_numbers = ['A', 1, 4, 'B', 5, 'C', 2, 6]
list_comp_4 = [x if type(x) == str else x * 5 for x in my_numbers]
print(list_comp_4)

#  ВЛОЖЕННЫЕ СПИСКИ
# ГЕНЕРАЦИЯ ДВУХ ЭЛЕМЕНТОВ

# ПРИМЕР № 5

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
they_number = [2, 7, 1, 8, 2, 8, 1, 8]

result = [x * y for x in my_numbers for y in they_number]
print(result)

#  операция умножения "x×y" будет выполняться только в том случае,
#  если остаток от деления "x" на 2 больше нуля,  если «x» нечетное (x%2 > 0)
result = [x * y for x in my_numbers for y in they_number if x % 2]
print(result)

# Можно добавить дополнительное условие, объединяя несколько проверок в одном выражении
# с помощью логических операторов, таких как «and», «or» и «not».
# если «x» нечетное (x%2 > 0), а «y» делится на 2, то будем добавлять произведение «x * y» в список result
result = [x * y for x in my_numbers for y in they_number if x % 2 and y // 2]
print(result)

#   ГЕНЕРАТОРЫ
# Генераторы позволяют создавать коллекции данных не занимая лишней памяти,
# что делает их особенно полезными для работы с большими объёмами данных
# Например, чтобы создать множество, можно использовать генератор с ФИГУРНЫМИ СКОБКАМИ.
# В множестве элементы уникальны, и при добавлении новых элементов повторяющиеся автоматически исключаются.
# Кроме того, элементы в множестве упорядочиваются по возрастанию.

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = {x for x in my_numbers}
print(result)

# Точно так же, как и множества, мы можем генерировать "словари" с помощью генераторов.
# вместо простого значения мы указываем пару "ключ:значение"
result = {x: x**2 for x in my_numbers}
print(result)

#    ОБЬЕДИНЕНИЕ СПИСКОВ
#В переменную third_result запишите словарь созданный при помощи сборки,
# где парой ключ-значение будет строка-длина строки.
# Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки.
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

third_result = {x:len(x) for x in first_strings + second_strings if not len(x) % 2 }
print(third_result)