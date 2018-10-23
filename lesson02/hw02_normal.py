
__author__ = 'Rina Zubko'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь. Вывести результат
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

n = int(input('Введите количество элементов списка равное n: '))
a = []

while n > 0:
    a.append(random.randint(-100, 100))
    n -= 1

print('Получили произвольный список из n элементов: ', a)

a = [x for x in a if x >= 0]
a = [x for x in a if (math.sqrt(x) - int(math.sqrt(x))) == 0]

print('Корни элементов исходного списка (если результаты извлечения корня не имеют десятичной части и такой \
корень вообще можно извлечь', a)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое', \
'07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое', '12': 'двенадцатое', \
'13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', \
'18': 'восемндацатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', \
'22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', \
'26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', \
'30': 'тридцатое', '31': 'тридцать первое',}

month = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля', \
'08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}

date = input('Введите дату: ')

dd = date[0:2]
mm = date[3:5]
yyyy = date[6:]

print(day[dd] + ' ' + month[mm] + ' ' + yyyy + ' года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
# выведите созданный список

n = int(input('Введите количество элементов списка равное n: '))
a = []

while n > 0:
    a.append(random.randint(-100, 100))
    n -= 1

print('Получили произвольный список из n элементов: ', a)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
# выведите результаты

import random

n = int(input('Введите количество элементов списка равное n: '))
a = []

while n > 0:
    a.append(random.randint(0, 9))
    n -= 1

print('Получили произвольный список из n элементов: ', a)

uniqueValues = list(set(a))

print('Новый список, элементами которого являются неповторяющиеся элементы исходного списка: ', uniqueValues)

singleValues = [x for x in a if a.count(x) == 1]

print('Новый список с элементами исходного списка, которые не имеют повторений: ', singleValues)

# Задача - 4 б) - Второй вариант

Counts = {}

for x in a:
    if x in Counts:
        Counts[x] += 1
    else:
        Counts[x] = 1

singleValues = []

for key in Counts:
    if Counts[key] == 1:
        singleValues.append(key)

print('Новый список с элементами исходного списка, которые не имеют повторений: ', singleValues)
