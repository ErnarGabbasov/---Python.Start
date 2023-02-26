from math import *
# Пример 1
def task_1(A):
    sum = 0
    for i in A:
        if i > 0:
           sum += i
    return sum


# Пример 2
def task_2(A):
    sum = 0
    for i in A:
        sum += i
    sr = sum/len(A)
    return sr


# Пример 3
def task_3(A):
    sum = 0
    for i in A:
        sum += i
    sr = sum/len(A)
    B = list()
    for i in A:
        j = i - sr
        B.append(j)
    sum2 = 0
    for i in B:
        sum2 += i**2
    srz = sqrt(sum2/len(B))
    return srz
