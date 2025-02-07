def f1(number):
    return total / number

def f2():
    print('Какой хороший день')
    summ = 0
    for i in range(-2, 2, 1):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError and NameError  as exc:
            print(f'в нутри f1 что-то пошло не так - {exc}, но мы устояли')
    return summ / 0

try:
    total = f2()
    print(f'Вот результат функции: {total}')
except ZeroDivisionError or NameError as exc:
    print(f'в нутри f2 что-то пошло не так - {exc}, но мы устояли')