#      Функции - генераторы
# Вычисляем индексы всех слов заданных переменной "word" в текстовом файле "lesson_54.txt"


def find_word(f, word):
    g_indx = 0          # Смещение индекса в соответствии со строкой
    for line in f:      # читаем файл по строчно
        indx = 0        # индекс вхождения данного слова в эту строку
        while(indx != -1):
            indx = line.find(word, indx)    # с помощью find ищем в строке line слово word с индекса indx
            if indx > -1:                   # проверяем indx, если метод find не нашел слово word то он возвращает знач. -1
                yield g_indx + indx         # возвр-м гобал.индекс + индекс найденного слова
                indx += 1                   # увеличиваем индекс на 1, ч-бы продолжить с индекса после найденого слова
        g_indx += len(line)                 # увеличиваем гобал.индекс на длинну строки


try:
    with open("lesson_54.txt", encoding="utf_8") as file:
        a = find_word(file, "генератор")
        print(list(a))
except FileNotFoundError:
    print("Файл не найден")
except:
    print("Ошибка обработки файла")