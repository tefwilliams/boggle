import numpy as np
from nptyping import Int, String, NDArray, Shape
from dictionary import Dictionary

Array2x2Int = NDArray[Shape["2, 2"], Int]
Array4x4Str = NDArray[Shape["4, 4"], String]


unit_steps: list[Array2x2Int] = [
    np.array([-1, 0]),
    np.array([-1, 1]),
    np.array([0, 1]),
    np.array([1, 1]),
    np.array([1, 0]),
    np.array([1, -1]),
    np.array([0, -1]),
    np.array([-1, -1]),
]


class BoggleGrid:
    def __init__(self, grid: Array4x4Str, dictionary: Dictionary) -> None:
        validate_grid(grid)
        self.__grid = grid
        self.__dictionary = dictionary

    def get_all_words(self):
        '''
        Gets all valid Boggle words from the grid.
        '''
        rows, cols = self.__grid.shape
        return set(
            word
            for row in range(rows)
            for col in range(cols)
            for word in self.__get_words(np.array([row, col]), [])
        )

    def __get_words(
        self,
        current_coord: Array2x2Int,
        previously_visited: list[Array2x2Int]
    ) -> list[str]:
        '''
        Gets words starting at current coordinate (including previously visited letters) by
        recusively stepping through the grid. Will visit squares adjacent to the current
        square only if there are any valid words starting with the current string.
        '''
        current_string = self.__get_string(
            previously_visited + [current_coord])

        return [
            word
            for coord in (
                self.__get_adjacent_squares(current_coord, previously_visited)
                # Exit early if no words begin with current string
                if self.__dictionary.any_words_begin_with(current_string)
                else []
            )
            for word in self.__get_words(coord, previously_visited + [current_coord])
        ] + ([current_string] if self.__dictionary.is_valid_word(current_string) else [])

    def __get_string(self, coords: list[Array2x2Int]) -> str:
        return "".join(
            str(self.__grid[*coord])
            for coord in coords
        )

    def __get_adjacent_squares(
        self,
        current_square: Array2x2Int,
        previously_visited: list[Array2x2Int]
    ):
        '''
        Gets the coordinates of all squares surrounding the current square.
        Excludes those that are outside of the grid (i.e. if the current square is at an edge)
        and any squares that have previously been visited.
        '''
        return [
            adjacent_square for adjacent_square
            in current_square + unit_steps
            if (
                self.__within_grid(adjacent_square) and
                # Check adjacent_square not in previously_visited
                all(not np.all(adjacent_square == array)
                    for array in previously_visited)
            )
        ]

    def __within_grid(self, coord: Array2x2Int):
        '''
        Checks whether the given coordinates are within the grid.
        '''
        num_rows, num_cols = self.__grid.shape
        row_num, col_num = coord
        return (
            0 <= row_num < num_rows and
            0 <= col_num < num_cols
        )


def validate_grid(grid: Array4x4Str):
    if grid.shape != (4, 4):
        raise ValueError(f'Grid shape should be (4, 4) - is {grid.shape}')

    invalid_squares = set(
        square
        for row in grid
        for square in row
        if not square.isalpha()
    )

    if any(invalid_squares):
        raise ValueError(
            f'Invalid value(s) for square: {", ".join(invalid_squares)}')
