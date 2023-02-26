from math import *
# Пример 1
def task_1(a, b):
    if(a > b):
        x = (sqrt(a*b) - 3)
    if(a == b):
        x = (log10(2))
    if(a < b):
        x = ((log(a**3 + 1))/(b))
    return x


# Пример 2
def task_2(a, b):
    if (a < b):
        x = (tan(a/b) + 1)
    if (a == b):
        x = (tan(-1))
    if (a > b):
        x = ((sqrt(a*b-5))/(a))
    return x


# Пример 3
def task_3(a, b):
    if (a > b):
        x = (log10(a*b) + 21)
    if (a == b):
        x = (tan(-5))
    if (a < b):
        x = (log(3 * a/b) + 1)
    return x


# Пример 4
def task_4(a, b):
    if (a > b):
        x = (sqrt(a * b - 1))
    if (a == b):
        x = (log10(255))
    if (a < b):
        x = ((tan(a - 5))/(b))
    return x


# Пример 5
def task_5(a, b):
    if (a > b):
        x = (log(a/b) + 31)
    if (a == b):
        x = (tan(-25))
    if (a < b):
        x = ((cos(a*5-1))/(a))
    return x


# Пример 6
def task_6(a, b):
    if (a < b):
        x = (sqrt(b/a + 1))
    if (a == b):
        x = (sqrt(25))
    if (a > b):
        x = ((log10(a**3 - 5))/(b))
    return x
