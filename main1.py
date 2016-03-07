import math  # математические функции
import matplotlib.pyplot as plt
import graphic1  # 32 строка
import find_cross_line as fcr
from random import randint as rand

# import array

# start_n = int(input("начальное число вершин от 5 до 10:"))
# start_n = rand(5, 10)
start_n = 8
if start_n < 5:
    start_n = 5
if start_n > 10:
    start_n = 10
print("начальное число вершин", start_n)

start_m = 20
# start_m = rand(5, 6)
# start_m = int(input("число итераций от 5 до 20:"))
print("число итераций", start_m)

pointsall = []  # объявляю пустой список

for i in range(start_n):  # создание списка координат вершин многогранника
    #  pointsx = pointsx + [round(math.sin(2 * math.pi * i / start_n), 3)]
    #  pointsy = pointsy + [round(math.cos(2 * math.pi * i / start_n), 3)]
    pointsall = pointsall + \
                [[round(math.sin(2 * math.pi * i / start_n), 4), round(math.cos(2 * math.pi * i / start_n), 4)]]

linesall = pointsall + [pointsall[0]]  # список линий включает повторяющееся точки, а список точек - нет
print(pointsall, "все линии:", linesall, sep='\n')

"""Для инициации процесса первая линия проводиться вручную,
чтобы точка начала и конца не вопали в выбор для новой линии"""

chose1 = rand(2, len(pointsall) - 2)  # первая итерация на многограннике исключает начальную точку и две рядом
next_point1 = pointsall[chose1]  # выбор точки, куда потянеться линя из первой точки
# next_line = [pointsall[0], next_point]  # создание линии для проверки на совпадение
print("первая случайная:", chose1, "длина всех точек минус 1:", len(pointsall) - 1)
linesall = linesall + [next_point1]  # дополнене списка линий еще одной
print("все точки:", pointsall, "все линии:", linesall, sep='\n')

"""Для выбора второй точки надо учесть, что список точек не увеличился и надо исключить последнюю точку линий"""

temppoints = pointsall[:]  #создание временного списка для второй линии
# temppoints = [pointsall[1:chose1 - 1], pointsall[chose1 + 1:]]
# del temppoints[0]
temppoints.remove(pointsall[chose1 + 1])  #удаление точки к которой пришла линия и двух рядом
temppoints.remove(pointsall[chose1])
temppoints.remove(pointsall[chose1 - 1])
temppoints.remove(pointsall[0])
chose2 = rand(0, len(temppoints) - 1)  # первая итерация на многограннике исключает начальную точку и следующую
next_point2 = temppoints[chose2]  # выбор точки, куда потянется линия из первой точки
linesall = linesall + [next_point2]  # дополнене списка линий еще одной
point_index = pointsall.index(next_point2)  #индекс для передачи в функцию поиска новой линии
print(point_index, "список точек 2:", temppoints)
print("все точкии:", pointsall, "все линии:", linesall, sep='\n')
temppoints.clear()

"""после построения двух линий дальнейшие действия ведутся через функцию"""


def finde_all_cross(linesall_f):
    """передать список всех линий,
    поиск имеет смысл начинать с эн+2-й линии"""
    next_line_f = [linesall_f[-2], linesall_f[-1]]  # последняя линия
    point_cross_f = []
    """разобраться с range(start_n, len(linesall_f) - 2) - чтобы работал без ошибок"""
    for k in range(start_n, len(linesall_f) - 2):  #перебор по очереди всех линий с эн и без 2 последних пересечения нет
        add_cross = [fcr.findcross(next_line_f, [linesall_f[k], linesall_f[k + 1]])]
        if add_cross != []:
            point_cross_f = point_cross_f + add_cross
    return point_cross_f

# print((next_point in pointsall))  #элемент есть в списке
# equal_line = abs(pointsall.index(next_point) - pointsall.index(pointsall[len(pointsall) - 1]))

for j in range(start_m - 2):
    next_point = fcr.chose_poit(point_index, pointsall, linesall)
    # print("следующая точка", next_point)
    point_index = pointsall.index(next_point)
    # print("индекс", point_index)
    linesall = linesall + [next_point]
    # print("все линии", linesall)
    point_cross = finde_all_cross(linesall)
    # print("cross:", point_cross)

    for j in range(len(point_cross)):
        check = 0
        if pointsall.count(point_cross[j]) == 0:
            pointsall = pointsall + [point_cross[j]]
    # print("все точки", pointsall)

print("все линии", linesall)
pointsx = []
pointsy = []

for i in range(len(linesall)):
    pointsx = pointsx + [linesall[i][0]]
    pointsy = pointsy + [linesall[i][1]]

plt.plot(pointsx, pointsy)  #нарисовать линии по списку координат
# graphic1.save("picture1")  #сохранение картинки на диск
"""for i in range(len(pointsx)):  #подписи координат к вершинам
    plt.text(pointsx[i], pointsy[i], str([pointsx[i], pointsy[i]]))"""
plt.axis([-2, 2, -2, 2])  #размер поля для вывода графика
plt.show()  #показать окно с графикой
