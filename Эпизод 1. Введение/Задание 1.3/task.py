from math import *
# Пример 1
def task_1(n):
    x = 0
    i = 1
    while(i <= n):
        x += 1 / i
        i += 1
    return x


# Пример 2
def task_2(x, n):
    y = 0
    y = y + x
    i = 3
    while(i <= n):
        y += x/i
        i += 2
    return y


# Пример 3
def task_3(n):
    x = factorial(n)
    return x


# Пример 4
def task_4(x, n):
    n = 9
    x = 1
    y = 1
    for i in range(2, n + 1):
        x *= (y + i)/i
    return x


# Пример 5
def task_5(x, n):
    n = 3
    x = 0
    y = 1
    for i in range(1, n + 1):
        x += (y * i)/(2 * i)
    return x


# Пример 6
def task_6(n):
    i = 2
    z = 1
    while(i <= n):
        z *= i
        i += 2
    return z
