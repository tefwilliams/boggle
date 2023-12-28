from boggle import get_words
from vector import Vector
from file_helpers import load_grid

grid = load_grid("./data/grid.csv")

words = []
for i in range(4):
    for j in range(4):
        words += get_words(grid, Vector(i, j))

words = set(words)

print(grid)
print(sorted(words))
