# todo: replace this with an actual task
def task_1(str):
    a = list()
    a = str.split()
    return len(a[len(a)-1])


def task_2(str):
    a = list()
    a = str.split()
    for i in range(0, len(a) - 1,2):
        a[i], a[i+1] = a[i+1], a[i]
    return " ".join(a)


def task_3(str):
    a = list()
    a = str.split()
    i = 1
    c = 1
    for i in range(len(a)-1):
        s = list(a[i])
        s2 = list(a[i-1])
        if (s[0] == (s2[len(s2)-1])):
            c += 1
    return c
