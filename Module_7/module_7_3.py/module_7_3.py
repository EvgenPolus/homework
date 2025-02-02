import string
class WordsFinder:
    file_names = ()
    def __init__(self, *name):
        self.file_names += name
        # print(self.file_names)
    all_words = {}
    def get_all_words(self):
        for f_name in self.file_names:
            #print(f_name)
            with open(f_name,'r', encoding='utf-8') as file:
                line  = file.read().rstrip("\n").lower()            # обрезаем "\n" в конце строки и переводим в ниний регистр
                table = str.maketrans("", "", string.punctuation)   # создание таблицы перевода символов
                line = line.translate(table)                        # применение таблицы к строке
                line = line.split()                                 # Разбиваем строку на элементы списка
                self.all_words[f_name] = line                       # создаем словарь с ключем f_name и значением line
        return self.all_words

    def find(self, word):
        word = word.lower()
        num_wrd = {}
        for name, words in self.get_all_words().items():
            if word in words:
                for num, content in enumerate(words, 1):            # перебираем и нумеруем с 1, слова из строки words
                    if word == content:                             # ищем совпадение искомого текста
                        num_wrd[name] = num                         # создаем словарь с ключем name и значением num
                        break                                       # прерываем поиск при первом совпадении
        return num_wrd

    def count(self, word):
        word = word.lower()
        num_wrd = {}
        cnt_wrd = int(0)
        for name, words in self.get_all_words().items():
            if word in words:
                for content in words:
                    if word == content:
                        cnt_wrd += 1
                        num_wrd[name] = cnt_wrd
        return num_wrd






finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего