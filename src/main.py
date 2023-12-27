from boggle import get_words
from coordinate import Coordinate
from file_helpers import load_grid

grid = load_grid("./data/grid.csv")

words = []
for i in range(4):
    for j in range(4):
        words += get_words(grid, Coordinate(i, j))


print(grid)
print(words)
