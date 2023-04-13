import csv


class Calculator:  # Создаем класс
    def __init__(self):
        self.num1 = int(input('Введите первое число: '))
        self.num2 = int(input('Введите второе число: '))

    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


# Создание объекта класса Calculator
calculator = Calculator()

# Вызов методов класса Calculator
print("Сумма:", calculator.sum())
print("Разность:", calculator.sub())
print("Произведение:", calculator.mult())
print("Частное:", calculator.div())

# Exercise_h_w
class Count:

    def __init__(self, input_):
        self.len_input_ = len(str(input_))
        self.input_ = input_

    def method_1(self):
        consonants = []
        vowels = []
        if isinstance(self.input_, str):
            for i in self.input_:
                if i in 'аяуюоеэиыАЯУЮОЕЭИЫ':
                    vowels.append(i)
                elif i == ' ':
                    pass
                else:
                    consonants.append(i)
            if len(vowels) * len(consonants) <= self.len_input_:
                return vowels
            else:
                return consonants
        if isinstance(self.input_, int):
            return self.len_input_ * sum([int(i) for i in str(self.input_) if int(i) % 2 == 0])


input_1 = Count('Привет')
input_2 = Count(123456)
print(input_1.method_1())
print(input_2.method_1())


# EXERCISE3
class Employee:  # Создаем класс Сотрудник с атрибутами (имя, фамилия, должность, зарплата)
    def __init__(self, name, surname, job_title, salary):  # Инициализируем
        self.name = name
        self.surname = surname
        self.job_title = job_title
        self.salary = salary

    def set_name(self, name):  # Создаем метод для  имени
        self.name = name

    def set_surname(self, surname):  # Создаем метод для фамилии
        self.surname = surname

    def set_position(self, job_title):  # Создаем метод для должности
        self.job_title = job_title

    def set_salary(self, salary):  # Создаем метод для зарплаты
        self.salary = salary
        self.write_to_csv()

    def increase_salary(self, percent): # Создаем метод для изменения зарплаты
        self.salary *= (1 + percent / 100)
        self.write_to_csv()

    def compare_salary(self, other):  # Создаем метод для сравнения зарплаты
        if self.salary > other.salary:
            return f"{self.name} {self.surname} зарабатывает больше, чем {other.name} {other.surname}"
        elif self.salary < other.salary:
            return f"{self.name} {self.surname} зарабатывает больше, чем {other.name} {other.surname}"
        else:
            return f"{self.name} {self.surname} зарабатывает больше, чем {other.name} {other.surname}"

    def write_to_csv(self):
        with open('employees.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.surname, self.job_title, self.salary])

    def display_info(self):  # Создаем метод для записи изменения зарплаты в файл
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Должность: {self.job_title}")
        print(f"Зарплата: {self.salary}")


# Создание объектов класса "Сотрудник"
employee1 = Employee("Марина", "Ефимова", "Инженер", 2700)
employee2 = Employee("Егор", "Белов", "Механик", 2200)
employee3 = Employee("Сергей", "Мацуль", "Механик", 2000)
employee4 = Employee("Максим", "Котов", "Монтер", 1300)
employee5 = Employee("Татьяна", "Заяц", "Инженер", 2700)
employee6 = Employee("Сергей", "Зубов", "Главный нженер", 3700)
employee7 = Employee("Андрей", "Паль", "Механик", 2100)


# Изменение атрибутов объектов
employee1.set_position("Директор")
employee2.set_salary(2100)

# Вывод информации о сотрудниках на экран
employee1.display_info()
employee2.display_info()
employee3.display_info()
employee4.display_info()
employee5.display_info()
employee6.display_info()
employee7.display_info()

# Изменение зарплаты на  значение и увеличение зарплаты на заданное процентное значение
employee1.set_salary(3000)
employee2.increase_salary(10)

# Сравнение зарплаты текущего объекта с зарплатой другого объекта класса
print(employee1.compare_salary(employee2))



