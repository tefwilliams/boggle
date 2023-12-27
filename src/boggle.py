from coordinate import Coordinate
from words import dictionary

surrounding_letters = [
    Coordinate(-1, 0),
    Coordinate(-1, 1),
    Coordinate(0, 1),
    Coordinate(1, 1),
    Coordinate(1, 0),
    Coordinate(1, -1),
    Coordinate(0, -1),
    Coordinate(-1, -1),
]


def get_words(grid, current_letter: Coordinate, previously_visited: list[Coordinate] = []):
    current_word = "".join(grid[*coord]
                           for coord in previously_visited) + grid[*current_letter]

    valid_words: list[str] = [
        current_word] if dictionary.check(current_word) and len(current_word) >= 3 else []

    if not any(word.startswith(current_word) for word in dictionary.suggest(current_word)):
        return valid_words

    # Get adjacent squares for any square
    next_letters = [
        letter + current_letter
        for letter in surrounding_letters
    ]

    grid_shape = grid.shape
    next_letters = [
        letter for letter in next_letters
        if (
            within_grid(letter, grid_shape) and
            letter not in previously_visited
        )
    ]

    for letter in next_letters:
        valid_words += get_words(grid, letter,
                                 previously_visited + [current_letter])

    return valid_words


def within_grid(coord: Coordinate, grid_shape: tuple[int, int]):
    return (
        coord.row >= 0 and
        coord.col >= 0 and
        coord.row < grid_shape[0] and
        coord.col < grid_shape[1]
    )
