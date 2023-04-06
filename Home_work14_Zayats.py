import json
from pprint import pprint
# Создаем пустой список, в который будем добавлять каждую покупку
shopping_list = []
# Создаем цикл
while True:
    # Запрашиваем у пользователя назввание и стоимость покупки
    name_ = input("Введите название своей покупки или 'стоп' для завершения: ")
    # Если пользователь вводит ' стоп', то выходим из цикла
    if name_ == 'стоп':
        break
    price = float(input("Введите стоимость покупки:"))
    #  Иначе добавляем покупку в список в виде словаря с ключами
    shopping_list.append({'Покупка': name_,'Стоимость': price})
# Записываем список в файл с помощью функции json.dump()
with open("shopping_list.json", "w") as file:
    json.dump(shopping_list, file, ensure_ascii=False)
# Создаем переменную для подсчета стоимости покупок
total_price = 0
# Читаем файл и выводим стоимость покупок
with open('shopping_list.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    pprint(data)
    for shopping_list in data:
        total_price += shopping_list['Стоимость']

print(f'Общая стоимость всех покупок: {total_price}')

