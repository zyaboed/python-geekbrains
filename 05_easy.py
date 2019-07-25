# coding: utf-8

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
import sys

# создание

def making():
    try:
        for i in range(1, 10):
            os.mkdir("dir_" + str(i))
            print(f'Папка dir_{str(i)} создана')
    except:
        print("Папка уже существует")

if __name__ == '__main__':
    making()
    

# удаление созданных папок

def remove():
    try:
        for i in range(1, 10):
            os.rmdir("dir_" + str(i))
            print(f'Папка dir_{str(i)} удалена')
    except:
        print("Папка не найдена")

if __name__ == '__main__':
    remove()




# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def display():
    folder = os.listdir()
    for i in folder:
        print(i)

if __name__ == '__main__':
    display()
        



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def file_copy ():
    name = os.path.realpath(__file__)
    new_ = name + '.cop'
    if os.path.isfile(new_) != True:
        shutil.copy(name, new_)
        return 'Файл  ' + name + ' скопирован - ' + new_
    else:
        return 'Копия уже сделана'

print(file_copy())


