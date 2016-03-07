import sympy.geometry as symg
from random import randint as rand


def findcross(one_line, second_line):
    """Линии состоят из [[x1,y1],[x2,y2]] для поиска пересечений,
    исключая крайние точки. Если пересечения нет, на выходе """
    x1, y1, x2, y2 = one_line[0][0], one_line[0][1], one_line[1][0], one_line[1][1]
    x3, y3, x4, y4 = second_line[0][0], second_line[0][1], second_line[1][0], second_line[1][1]
    p1, p2, p3, p4 = symg.Point(x1, y1), symg.Point(x2, y2), symg.Point(x3, y3), symg.Point(x4, y4)
    l1, l2 = symg.Line(p1, p2), symg.Line(p3, p4)
    pointxy = symg.intersection(l1, l2)
    if pointxy != []:
        pointxy = [round(pointxy[0].x, 4), round(pointxy[0].y, 4)]
    return pointxy

# print(findcross([[1, 0], [1, 1.01]], [[0, 0], [2, 1.33]]))


def chose_poit(point_index_f, pointsall_f, lines_all_f):
    """point_index_f - индекс последней точки
    pointsall_f - список всех точек
    выбор следующей точки по критерию уникальности новой линии, возвращает точку [x,y]"""
    one_more = 1
    while one_more == 1:
        chose1_f = point_index_f
        while chose1_f == point_index_f:
            chose1_f = rand(0, len(pointsall_f) - 1)  # чтобы не было совпадений с точкой начала
        next_point1_f = pointsall_f[chose1_f]  # выбор точки, куда потянеться линя из первой точки
        p01 = symg.Point(pointsall_f[point_index_f][0], pointsall_f[point_index_f][1])
        p02 = symg.Point(next_point1_f[0], next_point1_f[1])  # создание линии для проверки на совпадение
        one_more = 0
        for j in range(len(lines_all_f) - 1):
            p1 = symg.Point(lines_all_f[j][0], lines_all_f[j][1])
            p2 = symg.Point(lines_all_f[j + 1][0], lines_all_f[j + 1][1])
            if symg.Point.is_collinear(p1, p2, p01, p02) == True:
                one_more = 1
                break
    return next_point1_f
