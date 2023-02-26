from math import *

def task_1(text):
    str = text.strip('.').split('.')
    dict = {i.strip(): len(i.strip().split(' ')) for i in str}
    return dict


def task_2(x1,y1,x2,y2):
    L = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return L

