#  Exercise_h_w
""" Создаем декоратор debug, который выводит имя декорируемой функции,  аргумент
 и возвращаемое значение. Затем мы определили две функции: add и multiply, которые складывают
 и умножают два числа. Вызываем обе функции, обернув их в декоратор debug.
 При вызове каждой функции мы увидим информацию о переданных аргументах и возвращаемом значении."""


def debug(func):
    def wrapper(*args):
        print(f"Вызываемая функция {func.__name__} с аргументами: {args}")
        result = func(*args)
        print(f"Функция {func.__name__} возвращает результат {result} ")
        return result

    return wrapper


@debug
def add(a, b):
    return a + b


@debug
def multiply(a, b):
    return a * b


add(1, 4)
multiply(5, 6)

#  Exercise_2
'''Cоздаем декоратор count_calls, который считает количество вызовов функции, обернутой в декоратор. 
 Определяем две функции: get_multiples_of_three и get_non_multiples_of_three,
 которые возвращают список значений, кратных 3 и не кратных 3. 
 Мы вызвали обе функции для списка lst. Выводим получившиеся списки и их длину '''


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@count_calls
def get_mult_of_three(lst_):
    result = []
    for sublist in lst_:
        for num in sublist:
            if num % 3 == 0:
                result.append(num)
    return result


@count_calls
def get_non_mult_of_three(lst_):
    result = []
    for sublist in lst_:
        for num in sublist:
            if num % 3 != 0:
                result.append(num)
    return result


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

mult_of_three = get_mult_of_three(lst)
non_mult_of_three = get_non_mult_of_three(lst)

print("Список из значений кратных 3:", mult_of_three, "Длина списка:", len(mult_of_three))
print("Список значений не кратных 3:", non_mult_of_three, "Длина списка:", len(non_mult_of_three))
