class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
    def __add__(self, other):
        return f'Размер клетки равен: {self.quantity + other.quantity}'
    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клетка стала меньше, она равна: {sub} клеткам' if sub > 0 else 'Нулевое значение '
    def __truediv__(self, other):
        return self.quantity // other.quantity
    def __mul__(self, other):
        return self.quantity * other.quantity
    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result
cell = Cell(10)
cell_2 = Cell(2)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(7))