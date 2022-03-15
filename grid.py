from random import randint

from arrays import Array


class Grid:
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        """Retorna la altura o cantidad de filas de la matriz"""
        return len(self.data)

    def get_width(self):
        """Retorna el ancho o la cantidad de columnas de la matriz"""
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def randfill(self, min=0, max=100):
        """Rellena la matriz con datos random, con valores por defecto entre 0 y 100"""
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                self.data[i][j] = randint(min, max)

    def fill(self):
        """Rellena la matriz secuencialmente, comenzando a contar desde 1"""
        counter = 1
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                self.data[i][j] = counter
                counter += 1

    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"

        return str(result)
