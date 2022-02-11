from random import randint

from sort import bubble_sort

if __name__ == '__main__':
    array = [randint(1, 1000) for i in range(21)]
    bubble_sort(array)
    print(array)
