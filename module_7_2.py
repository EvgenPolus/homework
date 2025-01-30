
def custom_write(file_name, strings):

    with open(file_name, "w", encoding='utf-8') as file:
        for line in strings:
            file.write(f"{line}\n")


    with open(file_name, 'r', encoding='utf-8') as file:      # Чтение файла и разбиение его содержимого на строки
        strings_positions = {}

        for num_str in range(1, len(strings) + 1):             # перебор и нумерация строк с 1, по их коллич. len(lines)
            num_tell = file.tell()                             # читаем начальное положение курсора
            content = file.readline().rstrip("\n")             # запоминаем строку и убираем "\n" в конце стр.
            strings_positions[num_str, num_tell] = content     # создаем словарь с ключем: № стр. и № курсора в начале стр.
            #print(strings_positions)
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)