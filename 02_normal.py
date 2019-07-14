# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
import random
from math import sqrt

old = [2, -5, 8, 9, -25, 25, 4]
new = []
for i in old:
    if i >= 0:
        i = math.sqrt(i)
        if i % 1 == 0:
            new.append(int(i))
print(new)            


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

old_date = '02.11.2013'
old_date = old_date.split('.')
new_date = []
if old_date[0] == '01':
    new_date.append('первое')
elif old_date[0] == '02':
    new_date.append('второе')
elif old_date[0] == '03':
    new_date.append('третье')
elif old_date[0] == '04':
    new_date.append('четвертое')
elif old_date[0] == '05':
    new_date.append('пятое')
elif old_date[0] == '06':
    new_date.append('шестое')
elif old_date[0] == '07':
    new_date.append('седьмое')
elif old_date[0] == '08':
    new_date.append('восьмое')
elif old_date[0] == '09':
    new_date.append('девятое')
elif old_date[0] == '10':
    new_date.append('десятое')
elif old_date[0] == '11':
    new_date.append('одиннадцатое')
elif old_date[0] == '12':
    new_date.append('двенадцатое')
elif old_date[0] == '13':
    new_date.append('тринадцатое')
elif old_date[0] == '14':
    new_date.append('четырнадцатое')
elif old_date[0] == '15':
    new_date.append('пятнадцатое')
elif old_date[0] == '16':
    new_date.append('шестнадцатое')
elif old_date[0] == '17':
    new_date.append('семнадцатое')
elif old_date[0] == '18':
    new_date.append('восемнадцатое')
elif old_date[0] == '19':
    new_date.append('девятнадцатое')
elif old_date[0] == '20':
    new_date.append('двадцатое')
elif old_date[0] == '21':
    new_date.append('двадцать первое')
elif old_date[0] == '22':
    new_date.append('двадцать второе')
elif old_date[0] == '23':
    new_date.append('двадцать третье')
elif old_date[0] == '24':
    new_date.append('двадцать четвертое')
elif old_date[0] == '25':
    new_date.append('двадцать пятое')
elif old_date[0] == '26':
    new_date.append('двадцать шестое')
elif old_date[0] == '27':
    new_date.append('двадцать седьмое')
elif old_date[0] == '28':
    new_date.append('двадцать восьмое')
elif old_date[0] == '29':
    new_date.append('двадцать девятое')
elif old_date[0] == '30':
    new_date.append('тридцатое')
elif old_date[0] == '31':
    new_date.append('тридцать первое')
else:
    new_date.append('неизвестный формат даты')
    
if old_date[1] == '01':
    new_date.append('января')
elif old_date[1] == '02':
    new_date.append('февраля') 
elif old_date[1] == '03':
    new_date.append('марта')  
elif old_date[1] == '04':
    new_date.append('апреля')  
elif old_date[1] == '05':
    new_date.append('мая')  
elif old_date[1] == '06':
    new_date.append('июня')  
elif old_date[1] == '07':
    new_date.append('июля')  
elif old_date[1] == '08':
    new_date.append('августа')  
elif old_date[1] == '09':
    new_date.append('сентября')  
elif old_date[1] == '10':
    new_date.append('октября')  
elif old_date[1] == '11':
    new_date.append('ноября')  
elif old_date[1] == '12':
    new_date.append('декабря')  
else:
    new_date.append('нет такого месяца')    
    
new_date.append(old_date[2])   
d = new_date[0]
m = new_date[1]
y = new_date[2]
print(d, ' ', m, ' ', y, ' года')



# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

list = []
e = int(input('Введите число элементов в вашем списке: '))
while e > 0:
    x = random.randint(-100, 100)
    list.append(x)
    e -= 1
print(list)  



# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


first_list = [1, 2, 4, 5, 6, 2, 5, 2]
second_list = []
for i in first_list:
    if first_list.count(i) == 1:
        second_list.append(i)
print(second_list)
        


