# Exercise_1

# with open("text_1.txt", "r") as f:
#   sum_ = [int(i) for i in f.readline().split(' ') if i.isdigit()]
#   print(sum(sum_))


f = open("text_1.txt", "r")
words = f.read()
words.split('_' or ' ')
total = 0
for i in words:
    if i.isdigit():
        total += int(i)
print(total)

# Exercise_2


with open("text_2.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    numbers = []
    words_ = []
    for line in lines:
        if line.isdigit():
            numbers.append(int(line))
        else:
            words_.append(line)
        numbers = sorted(numbers)
        words_ = sorted(words_, key=lambda x: len(x))
        result = numbers + words_
    print(result)

# Exercise_3
with open('text_3.txt', 'w') as f:
    while True:
        line_1 = input('Введите строку(пустая строка для окончания ввода:')
        if line_1 == "":
            break
        f.write(line_1 + "\n")
f.close()

# Exercise_4
with open('text_4.txt', 'r') as f:
    lines_1 = f.readlines()
    num_lines = len(lines_1)
    for line in lines_1:
        num_chars = len(line.strip())
        print(f'Строка {line.strip()} содержит {num_chars} символов')
    print(f'В файле содержится {num_lines} строк')
f.close()

# Exercise_h_w

words_and_number = ['one', 2, 'three', 4, 'five', 6, 7, 8, 'ten']
# Выберем из массива слова и отсортируем их по длине
words_1 = sorted([word for word in words_and_number if isinstance(word, str)], key=len)
# Выберем из массива числа  и отсортируем их по возрастанию
numbers_1 = sorted([number for number in words_and_number if isinstance(number, int)])
# Запишем слова и числа в файл
with open('text_5.txt', 'w') as file:
    for word in words_1:
        file.write(f'{word}\n')
    for number in numbers_1:
        file.write(f'{number}\n')
