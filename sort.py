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
