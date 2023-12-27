from __future__ import annotations


class Coordinate(tuple[int, int]):
    def __new__(cls, row: int, col: int):
        return tuple.__new__(Coordinate, (row, col))

    def __init__(self, row: int, col: int):
        self.__row = row
        self.__col = col

    def __add__(self, other: Coordinate):
        return Coordinate(self.row + other.row, self.col + other.col)

    @property
    def row(self):
        return self.__row

    @property
    def col(self):
        return self.__col
