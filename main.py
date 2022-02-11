from random import randint

from sort import quick_sort

if __name__ == '__main__':
    array = [randint(1, 1000) for i in range(10)]
    quick_sort(array)
    print(array)
