def task_1(str):
    a = {}
    for i in str:
        if i.isalpha():
            if i.lower() in a:
                a[i.lower()] += 1
            else:
                a[i.lower()] = 1
    return a


def task_2(list):
    a = sum(set(list))
    return a


def task_3(cities):
    str = ', '.join(cities)
    str += '.'
    return str


def task_4(a, b):
    c = list(set(a) & set(b))
    return c
