
__author__ = 'Екатерина Зубко'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

a = int(input('Введите число a: '))
print('Число a состоит и следующих цифр:')

while a > 10:
    b = a % 10
    print(b)
    a = int(a / 10)

print(a)

# Задача-1: второй вариант

a = input('Введите число a: ')
print('Число a состоит и следующих цифр:')
for i in a:
    print(i)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

c = a

a = a - a + b
b = a - a + c

print('Число a = ' + str(a))
print('Число b = ' + str(b))

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

years = int(input('Скажите, пожалуйста, сколько Вам лет: '))

if years >= 18:
    print('Доступ разрешён.')
else:
    print('Извините, пользование данным ресурсом только с 18 лет.')
