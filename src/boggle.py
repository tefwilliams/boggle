from vector import Vector
from dictionary import is_valid_word, any_words_begin_with


    Vector(-1, 0),
    Vector(-1, 1),
    Vector(0, 1),
    Vector(1, 1),
    Vector(1, 0),
    Vector(1, -1),
    Vector(0, -1),
    Vector(-1, -1),
]


class BoggleGrid:
    def __init__(self, grid) -> None:
        self.__grid = grid

    def get_all_words(self):
        rows, cols = self.__grid.shape
        return set(
            word
            for row in range(rows)
            for col in range(cols)
            for word in self.__get_words(Vector(row, col))
        )

    def __get_words(self, current_coord: Vector, previously_visited: list[Vector] = []):
        current_string = self.__get_string(
            previously_visited + [current_coord])

        return [
            word
            for coord in (
                self.__get_adjacent_squares(current_coord, previously_visited)
                # Exit early if no words begin with current string
                if any_words_begin_with(current_string)
                else []
            )
            for word in self.__get_words(coord, previously_visited + [current_coord])
        ] + ([current_string] if is_valid_word(current_string) else [])

    def __get_string(self, coords: list[Vector]) -> str:
        return "".join(
            self.__grid[*coord]
            for coord in coords
        )

    def __get_adjacent_squares(self, current_square: Vector, previously_visited: list[Vector]):
        '''
        Gets the coordinates of all squares surrounding the current square.
        Excludes those that are outside of the grid (i.e. if the current square is at an edge)
        and any squares that have previously been visited.

        Parameters:
            grid: The grid of squares.
            current_square (Vector): The coordinates of the current square.
            previously_visited (list[Vector]): The coordinates of all squares that have previously been visited.

        Returns:
            adjacent_squares (list[Vector]): The list of unvisted adjacent squares.
        '''
        adjacent_squares = []
        for step in unit_steps:
            adjacent_square = step + current_square

            if (
                self.__within_grid(adjacent_square) and
                adjacent_square not in previously_visited
            ):
                adjacent_squares.append(adjacent_square)

        return adjacent_squares

    def __within_grid(self, coord: Vector):
        '''
        Checks whether the given coordinates are within a grid of the given shape.

        Parameters:
            coord (Vector): The coordinates.
            grid_shape (tuple[int, int]): The dimensions of the grid.

        Returns:
            within_grid (bool): Whether the given coordinates are within a grid of the given shape.
        '''
        rows, cols = self.__grid.shape
        return (
            coord.row >= 0 and
            coord.col >= 0 and
            coord.row < rows and
            coord.col < cols
        )
