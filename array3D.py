from arrays import Array
from grid import Grid


class Array3D:
    def __init__(self, depth, height, width):
        self.data = Array(depth)
        for i in range(depth):
            self.data[i] = Grid(height, width)

    def get_depth(self):
        """Retorna la profundidad del array3D"""
        return len(self.data)

    def get_height(self):
        """Retorna la altura"""
        return self.data[0].get_height()

    def get_width(self):
        """Retorna el ancho"""
        return self.data[0].get_width()

    def fill(self):
        """Rellena el array3D con valores en orden comenzando desde 1"""
        for i in range(self.get_depth()):
            counter = (self.get_height() * self.get_width() * i) + 1
            self.data[i].fill(counter)

    def __getitem__(self, item):
        return self.data[item]

    def rand_fill(self, min=0, max=1000):
        """Rellena el array3D con valores random en un rango que escoja el usuario.
        El rango por defecto es 0-1000"""
        for i in range(self.get_depth()):
            self.data[i].randfill(min, max)

    def __str__(self):
        result = ""
        for i in range(self.get_depth()):
            result += str(self.data[i])
            result += "-" * self.get_width() * 4
            result += '\n'

        return str(result)
