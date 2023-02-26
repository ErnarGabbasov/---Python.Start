import math
# Пример 1
def task_1(a, d, c):
    t1 = ((c - d/5 + math.sqrt(321))/(1 + a * 3))
    return t1


# Пример 2
def task_2(a, d, c):
    t2 = ((math.log10(c/3) - d + 25)/(a * 5 - 1))
    return t2


# Пример 3
def task_3(a, d, c):
    t3 = ((c/2 + math.log(d) - 35)/(a * 5 + 1))
    return t3


# Пример 4
def task_4(a, d, c):
    t4 = ((math.tan(c) + d/32)/(a/3 + 1))
    return t4


# Пример 5
def task_5(a, d, c):
    t5 = ((c/5-d+1)/(c + math.tan(2 * a)))
    return t5


# Пример 6
def task_6(a, d, c):
    t6 = ((math.sqrt(25 * c) + d-3)/(d - a * a + 1))
    return t6


# Пример 7
def task_7(a, d, c):
    t7 = ((5 * math.log10(c) + 3 * d - 32)/(a * a + 1))
    return t7


# Пример 8
def task_8(a, d, c):
    end = ((c * d - math.log(4*3*a))/(c+a-1))
    return end