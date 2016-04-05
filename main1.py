import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anima
import find_cross_line as fcr
from random import randint as rand

# start_n = int(input("начальное число вершин от 5 до 10:"))
start_n = 7

if start_n < 5:
    start_n = 5

if start_n > 10:
    start_n = 10

print("начальное число вершин", start_n)

start_m = 10
# start_m = int(input("число итераций от 5 до 20:"))
print("число итераций", start_m)

pointsall = []

# создание списка координат вершин многогранника
for i in range(start_n):
    pointsall = pointsall + [[np.sin(2 * np.pi * i / start_n), np.cos(2 * np.pi * i / start_n)]]

# список линий включает повторяющееся точки, а список точек - нет
linesall = pointsall + [pointsall[0]]
# print(pointsall, "все линии:", linesall, sep='\n')

"""Для инициации процесса первая линия проводиться вручную,
чтобы точка начала и конца не вопали в выбор для новой линии"""

# первая итерация на многограннике исключает начальную точку и две рядом
chose1 = rand(2, start_n - 2)
# выбор точки, куда потянеться линя из первой точки
next_point1 = pointsall[chose1]
# дополнене списка линий еще одной
linesall = linesall + [next_point1]

"""Для выбора второй точки надо учесть, что список точек не увеличился и надо исключить последнюю точку линий"""

# создание временного списка для второй линии
temppoints = pointsall[:]

# удаление точки к которой пришла линия и двух рядом
temppoints.remove(pointsall[chose1 + 1])
temppoints.remove(pointsall[chose1])
temppoints.remove(pointsall[chose1 - 1])
temppoints.remove(pointsall[0])

# первая итерация на многограннике исключает начальную точку и следующую
chose2 = rand(0, len(temppoints) - 1)

# выбор точки, куда потянется линия из первой точки
next_point2 = temppoints[chose2]

# дополнене списка линий еще одной
linesall = linesall + [next_point2]

# индекс для передачи в функцию поиска новой линии
point_index = pointsall.index(next_point2)
temppoints.clear()

"""после построения двух линий дальнейшие действия ведутся через функцию"""


def finde_all_cross(linesall_f):
    """передать список всех линий,
    поиск имеет смысл начинать с эн+2-й линии"""

    # последняя линия
    next_line_f = [linesall_f[-2], linesall_f[-1]]
    point_cross_f = []
    """разобраться с range(start_n, len(linesall_f) - 2) - чтобы работал без ошибок"""

    # перебор по очереди всех линий с эн и без 2 последних пересечения нет
    for k in range(start_n, len(linesall_f) - 2):
        add_cross = [fcr.findcross(next_line_f, [linesall_f[k], linesall_f[k + 1]])]

        if add_cross != [[]]:
            point_cross_f = point_cross_f + add_cross

    return point_cross_f

# print((next_point in pointsall))  #элемент есть в списке
# equal_line = abs(pointsall.index(next_point) - pointsall.index(pointsall[len(pointsall) - 1]))

for j in range(start_m - 2):
    next_point = fcr.chose_poit(point_index, pointsall, linesall)
    print("следующая точка", next_point)
    point_index = pointsall.index(next_point)
    # print("индекс", point_index)
    linesall = linesall + [next_point]
    # print("все линии", linesall)
    point_cross = finde_all_cross(linesall)
    # print("cross:", point_cross)

    for k in range(len(point_cross)):
        if pointsall.count(point_cross[k]) == 0:
            pointsall = pointsall + [point_cross[k]]

    # pointsall = pointsall + point_cross
    # print("все точки", pointsall)

print("все линии", linesall)
pointsx = []
pointsy = []

for i in range(len(linesall)):
    pointsx = pointsx + [linesall[i][0]]
    pointsy = pointsy + [linesall[i][1]]

"""for i in range(len(pointsx)):  #подписи координат к вершинам
    plt.text(pointsx[i], pointsy[i], str([pointsx[i], pointsy[i]]))"""
plt.axis([-2, 2, -2, 2])
ani = anima.ArtistAnimation(plt.figure(), plt.plot(pointsx, pointsy), interval=50, blit=True, repeat_delay=1000)
plt.show()
