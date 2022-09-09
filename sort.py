def bubble_sort(arr):
    max_length = len(arr) - 1
    for i in range(max_length):
        # Asumimos que esta ordenado para no hacer recorridos innesesarios
        sort = True
        for j in range(max_length - i):
            if arr[j] > arr[j + 1]:
                # Significa que falta ordenar
                sort = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # Se cumple siempre y cuando no se haya ordenado nada
        if sort:
            break


def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i
        while (j > 0) and (arr[j] < arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        i += 1


def selection_sort(arr):
    max_length = len(arr)
    for i in range(max_length):
        # Encuentra el valor minimo desde la i
        min_value = min(arr[i:])
        if min_value != arr[i]:
            # ubica el index del nuevo minimo y los intercambia
            new_index = arr[i:].index(min_value) + i
            arr[i], arr[new_index] = arr[new_index], arr[i]


def quick_sort(arr):
    def partition(start, end, array):
        pivot = array[end]
        i = start
        for j in range(start, end):
            if array[j] <= pivot:
                array[i], array[j] = array[j], array[i]
                i += 1

        array[i], array[end] = array[end], array[i]

        return i

    def recursion(start, end, array):
        if start < end:
            p = partition(start, end, array)
            recursion(start, p - 1, array)
            recursion(p + 1, end, array)

    recursion(0, len(arr) - 1, arr)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        # main list
        k = 0
        while (i < len(left_arr)) and (j < len(right_arr)):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

#hola mundo
