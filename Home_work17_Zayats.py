import string


class Alphabet:
    def __init__(self, language, letters_str):
        self.lang = language
        self.letters = list(letters_str)

    def print(self):  # Печатаем все буквы алфавита
        print(self.letters)

    def letters_num(self):  # Возвращаем количество букв в алфавите
        return len(self.letters)


class EngAlphabet(Alphabet):  # Английский алфавит
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return print("Hello, world!.")


eng_alphabet = EngAlphabet()
eng_alphabet.print()  # выводим все буквы английского алфавита
print(eng_alphabet.letters_num())  # выводим количество букв в алфавите
print(eng_alphabet.is_en_letter('F'))  # True
print(eng_alphabet.is_en_letter('Щ'))  # False
EngAlphabet.example()

# Exercise_h_w

""" Класс Tomato определяет состояние созревания помидора и методы для перехода на следующую
стадию и проверки, когда помидор созреет. Класс TomatoBush создает список обьектов класса Tomato и
определяет методы для перевода всех помидоров на следующую стадию и проверки, все ли помидоры созрели а
также сбора урожая. Класс Gardener определяет методы для работы с растением и сбора урожая"""


class Tomato:
    states = {
        1: "зеленый",
        2: "желтый",
        3: "красный"
    }

    def __init__(self, index):
        self._index = index
        self._state = 1

    def grow(self):
        if self._state < 3:
            self._state += 1
        self.print_state()

    def is_ripe(self):
        return self._state == 3

    def print_state(self):
        print(f"Помидор {self._index} {Tomato.states[self._state]}")


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Начат сбор урожая")
            self._plant.give_away_all()
        else:
            print("Еще не все помидоры созрели, ожидайте")

    @staticmethod
    def knowledge_base():
        print("Справочник садовода:  чтобы вырастить помидоры, их нужно регулярно поливать,\n "
              "обеспечивать достаточное количество солнечного света и удобрять почву, используя \n"
              "белорусские калийные удобрения.")


# Тесты
Gardener.knowledge_base()

bush = TomatoBush(10)
gardener = Gardener("Василий", bush)

gardener.work()
gardener.work()
gardener.work()
gardener.work()
gardener.work()

gardener.harvest()

gardener.work()
gardener.work()
gardener.work()
gardener.work()
gardener.work()

gardener.harvest()
