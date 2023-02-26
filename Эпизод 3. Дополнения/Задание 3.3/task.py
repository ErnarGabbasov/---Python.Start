import fileinput


def task_1(l):
    return (max(l, key=l.count))

def task_2(x, y):
    n = 8
    flag = True
    for i in range(n):
        for j in range(i + 1, n):
            if (x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j])):
                flag = False
    if (flag):
        return 'NO'
    else:
        return 'YES'

def task_3(x, y, xc, yc, r):
    flag = True
    if ((x - xc) * (x - xc) + (y - yc) * (y - yc) == r * r):
        flag = True
    else:
        flag = False
    return flag

def task_4(a):
    count = 0
    for i in range(1, len(a) - 1):
        if ((a[i - 1] < a[i]) and (a[i] > a[i + 1])):
            count += 1
    return count


alfavit = 'abcdefghijklmnopqrstuvwxyz'
def task_5(key):
    f = open('file.txt', 'r')
    result = ''
    itog = []
    for line in f:
        line = line.lower().strip()
        for i in line:
            mesto = alfavit.find(i)
            new_mesto = mesto + key
            result += alfavit[new_mesto]
        itog.append(result)
        result = ''
    print(itog)
    return itog
