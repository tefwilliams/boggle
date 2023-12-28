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


def get_words(grid, current_square: Vector, previously_visited: list[Vector] = []):
    current_word = get_current_word(grid, current_square, previously_visited)
    valid_words = [current_word] if is_valid_word(current_word) else []

    if no_words_begin_with(current_word):
        return valid_words

    for square in get_next_letters(grid, current_square, previously_visited):
        valid_words += get_words(grid, square,
                                 previously_visited + [current_square])

    return valid_words


def get_current_word(grid, current_letter: Vector, previously_visited: list[Vector]) -> str:
    return "".join(
        grid[*coord]
        for coord in previously_visited
    ) + grid[*current_letter]


def is_valid_word(word: str):
    return dictionary.check(word) and len(word) >= 3


def no_words_begin_with(string: str):
    return not any(
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
