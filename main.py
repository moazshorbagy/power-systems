from importing_data import import_bus_data, import_line_data
from power_system import compute_y_bus_matrix, gauss_seidel


def main():
    # bus_data = import_bus_data()  # Parameters for all buses
    # line_data = import_line_data()  # Parameters and configuration for all lines

    bus_data = [
        [1, 0, 0, 1.04, 0],
        [3, -0.6, -0.4, 1, 0],
        [3, -0.6, -0.3, 1, 0],
        [2, 0.5, 0, 1.04, 0],
    ]

    line_data = [
        [0, 1, 0, 0.25],
        [0, 2, 0, 0.5],
        [0, 3, 0, 0.2],
        [1, 2, 0, 0.2],
        [2, 3, 0, 0.25],
    ]

    y_bus_matrix = compute_y_bus_matrix(4, line_data)
    gauss_seidel(bus_data, y_bus_matrix)


if __name__ == "__main__":
    main()
