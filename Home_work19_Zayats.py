""" Создаем итератор колоды карт, при вызове функции next() будет представлена следующая карта"""


class CardDeck:
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.suits) * len(self.ranks):
            raise StopIteration
        suit_ = self.suits[self.index // len(self.ranks)]
        rank_ = self.ranks[self.index % len(self.ranks)]
        self.index += 1
        return f"{rank_} {suit_}"


suit = ["Пик", "Треф", "Бубен", "Червей"]
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]

deck = CardDeck(suit, rank)
for card in deck:
    print(card)
print()

"""Итератор который получает на вход список чисел и возвращает кажлый третийй элемент списка"""
class EveryThird:
    def __init__(self, str1):
        self.string = str1

    def __iter__(self):
        self.index = 2
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        str2 = self.string[self.index]
        self.index += 3
        return str2


string = "123456789"
every_third = EveryThird(string)
for i in every_third:
    print(i, end=' ')
print()

"""Создаем функцию gener_a_strings, которая принимает список строк как аргумент,
 оператор yield возвращает список строк, в которых есть буква а"""


def gener_a_strings(strings_):
    for string_ in strings_:
        if 'a' in string_:
            yield string_


strings = ['abcd', 'abcda', 'bcd', 'abcda', 'sdfg']
gener_1 = gener_a_strings(strings)  # Создаем генератор вызывая функцию с аргументом strings
for string in gener_1:  # Цикл для итерации по генератору
    print(string, end=' ')  # Выводим каждую строку с буквой а
print()


"""Числа Фибоначчи рекурсия """
def fib_(num):
    if num <= 1:
        return num
    else:
        return fib_(num - 1) + fib_(num - 2)


result = []
for i in range(1, 9):
    result.append(fib_(i))

print(result)
