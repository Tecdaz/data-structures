from random import randint


class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        """Retorna la longitud del array"""
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        """Obtiene el valor de una posicion del array"""
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __sum__(self):
        """Retorna la sumatoria de los elementos dentro del array"""
        n = 0

        for i in range(len(self.items)):
            n += self.items[i]

        return n

    def rand_fill(self, min=0, max=100):
        """Rellena el array de valores random entre un rango especificado por el usuario.
        Su valor por defecto es un rango de 0-100"""
        for i in range(len(self.items)):
            self.items[i] = randint(min, max)

    def __fill__(self):
        """Rellena el array con valores desde 0 hasta la longitud del mismo"""
        for i in range(len(self.items)):
            self.items[i] = i
