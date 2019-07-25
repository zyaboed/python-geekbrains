# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py



# я не импортировала, а переписала функции из easy.py, они там под dir_1 - dir_9 были заточены
# hard не успеваю, извините

import os
import shutil
#import 05_easy
import sys

def change (path):
    try:
        os.chdir(path)
        return 'Вы перешли в папку -  {}'.format(path)
    except FileNotFoundError:
        return ('dir_{} - данная папка не найдена'.format(path))


def display():
    folder = os.listdir()
    for i in folder:
        print(i)

def remove(name):
    try:
        os.rmdir(name)
        print(f'Папка {name} удалена')
    except:
        print("Папка не найдена")

def making(name):
    try:
        os.mkdir(name)
        print(f'Папка {name} создана')
    except:
        print(f"{name} уже существует")

def start ():
    inp =''
    while inp != '0':
        print('Вы находитесь здесь: ' + os.getcwd())
        inp = input('\nВаш выбор:\n'
                       '1. Перейти в папку\n'
                       '2. Помотреть содержимое текущей папки\n'
                       '3. Удалить папку\n'
                       '4. Создать папку\n'
                       '0. Выход\n\n')
        if inp =='0':
            print('До новых встреч')
            break
        if inp == '1':
            path = input('Нужная папка -   ')
            print(change(path))
        elif inp == '2':
            display()
            #05_easy.display()
        elif inp == '3':
            name = input('Введите имя удаляемой папки - ')
            #05_easy.remove(name)
            remove(name)
        elif inp == '4':
            name = input('Введите имя новой папки - ')
            #05_easy.making(name)
            making(name)

if __name__ == '__main__':
    start()