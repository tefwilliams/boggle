from __future__ import annotations


class Vector(tuple[int, int]):
    # Replace with np array perhaps
    def __new__(cls, row: int, col: int):
        return tuple.__new__(Vector, (row, col))

    def __init__(self, row: int, col: int):
        self.__row = row
        self.__col = col

    def __add__(self, other: Vector):
        return Vector(self.row + other.row, self.col + other.col)

    @property
    def row(self):
        return self.__row

    @property
    def col(self):
        return self.__col
