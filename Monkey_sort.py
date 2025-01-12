import random
import time
a=[1,0,9]
def monkey_sort(a):
    while not is_sorted(a):
        random.shuffle(a)
        time.sleep(0.5)
        print(a)
    print(a)

def is_sorted(a):
    sorted = True
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            sorted = False
    return  sorted
monkey_sort(a)
