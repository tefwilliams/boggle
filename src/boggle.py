from words import dictionary

surrounding_letters: list[tuple[int, int]] = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]


def get_words(grid, current_letter: tuple[int, int], previously_visited: list[tuple[int, int]] = []):
    current_word = "".join(grid[*coord]
                           for coord in previously_visited) + grid[*current_letter]

    valid_words: list[str] = [
        current_word] if dictionary.check(current_word) and len(current_word) >= 3 else []

    if not any(word.startswith(current_word) for word in dictionary.suggest(current_word)):
        return valid_words

    # Get adjacent squares for any square
    next_letters: list[tuple[int, int]] = [
        [letter[0] + current_letter[0], letter[1] + current_letter[1]]
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


def within_grid(coord: tuple[int, int], grid_shape: tuple[int, int]):
    return (
        coord[0] >= 0 and
        coord[1] >= 0 and
        coord[0] < grid_shape[0] and
        coord[1] < grid_shape[1]
    )
