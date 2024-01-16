from numpy import loadtxt
from boggle import validate_grid


def load_grid(path: str):
    grid = loadtxt(path, dtype=str, delimiter=',')
    validate_grid(grid)
    return grid
