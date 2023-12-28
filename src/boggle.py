from vector import Vector
from words import dictionary


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
            get_next_letters(grid, current_coord, previously_visited)
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


def is_valid_word(word: str):
    return dictionary.check(word) and len(word) >= 3


def any_words_begin_with(string: str):
    return any(
        word.startswith(string)
        for word in dictionary.suggest(string)
    )


def get_next_letters(grid, current_square: Vector, previously_visited: list[Vector]):
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
    return (
        coord.row >= 0 and
        coord.col >= 0 and
        coord.row < grid_shape[0] and
        coord.col < grid_shape[1]
    )
