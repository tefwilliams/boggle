from vector import Vector
from dictionary import is_valid_word, any_words_begin_with


unit_steps = [
    Vector(-1, 0),
    Vector(-1, 1),
    Vector(0, 1),
    Vector(1, 1),
    Vector(1, 0),
    Vector(1, -1),
    Vector(0, -1),
    Vector(-1, -1),
]


def get_words(grid, current_coord: Vector, previously_visited: list[Vector] = []):
    current_string = get_string(grid, previously_visited + [current_coord])

    return [
        word
        for coord in (
            get_adjacent_squares(grid, current_coord, previously_visited)
            # Exit early if no words begin with current string
            if any_words_begin_with(current_string)
            else []
        )
        for word in get_words(grid, coord, previously_visited + [current_coord])
    ] + ([current_string] if is_valid_word(current_string) else [])


def get_string(grid, coords: list[Vector]) -> str:
    return "".join(
        grid[*coord]
        for coord in coords
    )


def get_adjacent_squares(grid, current_square: Vector, previously_visited: list[Vector]):
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
    grid_shape = grid.shape

    for step in unit_steps:
        adjacent_square = step + current_square

        if (
            within_grid(adjacent_square, grid_shape) and
            adjacent_square not in previously_visited
        ):
            adjacent_squares.append(adjacent_square)

    return adjacent_squares


def within_grid(coord: Vector, grid_shape: tuple[int, int]):
    '''
    Checks whether the given coordinates are within a grid of the given shape.

    Parameters:
        coord (Vector): The coordinates.
        grid_shape (tuple[int, int]): The dimensions of the grid.

    Returns:
        within_grid (bool): Whether the given coordinates are within a grid of the given shape.
    '''
    return (
        coord.row >= 0 and
        coord.col >= 0 and
        coord.row < grid_shape[0] and
        coord.col < grid_shape[1]
    )
