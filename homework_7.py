#1
class Matrix:
    def __init__(self, my_list):
        self.list = my_list

    def __str__(self):
        for i in self.list:
            for t in i:
                print(f"{t:4}", end="")

    def __add__(self, other):
        for i in range(len(self.list)):
            for i_2 in range(len(other.list[i])):
                self.list[i][i_2] = self.list[i][i_2] + other.list[i][i_2]
        return Matrix.__str__(self)

m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
m + new_m

#2
from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Smth vary abstract'

class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Smth vary abstract second'

class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass

coat = Coat(54)
costume = Costume(170)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())


#3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Размер клетки равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'теперь она равна: {sub} ' if sub > 0 else 'Клетка исчезла '

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

cell = Cell(24)
cell_2 = Cell(2)

print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(7))
