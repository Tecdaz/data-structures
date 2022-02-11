def bubble_sort(array):
    max_length = len(array) - 1
    for i in range(max_length):
        # Asumimos que esta ordenado para no hacer recorridos innesesarios
        sort = True
        for j in range(max_length - i):
            if array[j] > array[j + 1]:
                # Significa que falta ordenar
                sort = False
                array[j], array[j + 1] = array[j + 1], array[j]
        # Se cumple siempre y cuando no se haya ordenado nada
        if sort:
            break


def insertion_sort(array):
    i = 1
    while i < len(array):
        j = i
        while (j > 0) and (array[j] < array[j - 1]):
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        i += 1


def selection_sort(array):
    max_length = len(array)
    for i in range(max_length):
        # Encuentra el valor minimo desde la i
        min_value = min(array[i:])
        if min_value != array[i]:
            # ubica el index del nuevo minimo y los intercambia
            new_index = array[i:].index(min_value) + i
            array[i], array[new_index] = array[new_index], array[i]
