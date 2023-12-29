from boggle import BoggleGrid
from file_helpers import load_grid
from dictionary import Dictionary

grid = BoggleGrid(
    load_grid("./data/grid.csv"),
    Dictionary("en_GB")
)

words = grid.get_all_words()

print(f'Found {len(words)} words:')
for word in sorted(words):
    print(f' {word},')
