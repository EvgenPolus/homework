

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for num in numbers:
            result += num
    except TypeError as exc:
        incorrect_data += 1
        print(f'Некорректный тип данных для подсчёта суммы - {num}')

    return (result, incorrect_data)
    print(result, incorrect_data)

def calculate_average(numbers):
    average = 0
    # sum_num = personal_sum(numbers)
    try:
        average = personal_sum(numbers) / len(numbers)

    except ZeroDivisionError:
        return 0
    except TypeError:
        print(F'В numbers записан некорректный тип данных')
        return None

    return average


# print(personal_sum("1, 2, 3"))

# print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')