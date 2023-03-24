import numpy as np


def print_matrix(m):
    np.set_printoptions(precision=3)
    print(np.array(m))


def print_bus_data(m):
    np.set_printoptions(precision=3)
    print(["Type", "P", "Q", "V", "Delta"])
    print(np.array(m))
