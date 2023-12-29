from boggle import BoggleGrid
from file_helpers import load_grid

grid = BoggleGrid(
    load_grid("./data/grid.csv")
)

words = grid.get_all_words()

print(grid)
print(sorted(words))
