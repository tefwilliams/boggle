from numpy import loadtxt


def load_grid(path: str):
    return loadtxt(path, dtype=str, delimiter=',')
