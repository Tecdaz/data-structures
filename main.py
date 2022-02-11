from random import randint

from sort import bubble_sort, insertion_sort, selection_sort

if __name__ == '__main__':
    array = [randint(1, 1000) for i in range(20)]
    selection_sort(array)
    print(array)




