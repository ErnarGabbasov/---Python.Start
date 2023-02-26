def task_1(a, A):
    answer = a.index(A)
    return str(answer)


def task_2(a):
    flag = True
    for i in range(1, a):
        if((a % i == 0) and (i != a) and (i != 1)):
            flag = False
    return  flag