# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)** 2) + ((b_x - a_x)** 2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def perimeter(self):
        self.perimeter = (self.AB + self.BC + self.CA)
        return (self.perimeter)

    def area(self):
        self.perimeter /= 2
        self.area =  round(math.sqrt(self.perimeter * (self.perimeter - self.AB) * (self.perimeter - self.BC) * (self.perimeter - self.CA)), 2)
        return (self.area)

    def height(self):
        self.area *= 2
        self.height =  round((self.area / self.CA), 2)
        return (self.height)

trial = Triangle(4,4,8,9,9,3)


print('Длинна стороны АВ = {}, ВС = {}, СА = {}'.format(trial.AB, trial.BC, trial.CA))
print('Периметр треугольника = {}'.format(trial.perimeter()))
print('Площадь треугольника = {}'.format(trial.area()))
print('Высота треугольника, проведенная из угла В = {}'.format(trial.height()))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math


class Trapeze:
    def __init__(self, a, b, c, d):
       
        try:
            self.AB = round(math.sqrt((b[0]-a[0])** 2 + (b[1]-a[1])** 2), 2)
            self.BC = round(math.sqrt((c[0]-b[0])** 2 + (c[1]-b[1])** 2), 2)
            self.CD = round(math.sqrt((d[0]-c[0])** 2 + (d[1]-c[1])** 2), 2)
            self.DA = round(math.sqrt((a[0]-d[0])** 2 + (a[1]-d[1])** 2), 2)
        except TypeError:
            print('Вы ввели неверные параметры')

    def isosceles(self):
        return self.AB == self.CD

    def perimeter(self):
        return round(self.AB + self.BC + self.CD + self.DA, 2)

    def area(self):
    
        if self.isosceles():
            h = math.sqrt(self.AB ** 2 - ((self.DA - self.BC) ** 2) / 4)
            return round(1/2 * (self.BC + self.DA) * h, 2)
        else:
            p = self.perimeter() / 2
            return round((self.BC + self.DA) / abs(self.DA - self.BC) *
                         math.sqrt((p-self.DA) * (p-self.BC) *
                                   (p-self.DA-self.AB) *
                                   (p-self.DA-self.CD)), 2)


trial_tr = Trapeze((-2, 1), (-1, 3), (3, 4), (6, 3))

print('Это равнобокая трапеция? - {0}\n'
      'Площадь трапеции: {1} кв.см\nПериметр: {2} '
      'см'.format(trial_tr.isosceles(), trial_tr.area(), trial_tr.perimeter()))



