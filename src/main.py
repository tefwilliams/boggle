from boggle import get_words
from vector import Vector
from file_helpers import load_grid

grid = load_grid("./data/grid.csv")

words = set(
    word
    for i in range(4)
    for j in range(4)
    for word in get_words(grid, Vector(i, j))
)

print(grid)
print(sorted(words))
