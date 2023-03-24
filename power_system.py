import numpy as np

from utility import print_matrix, print_bus_data


def compute_y_bus_matrix(bus_count, line_data):
    y_bus_matrix = np.zeros((bus_count, bus_count)).tolist()

    # Calculate sum of admittances connected between buses
    for from_bus, to_bus, real, imag in line_data:
        y_bus_matrix[from_bus][to_bus] = -1 / complex(real, imag)
        y_bus_matrix[to_bus][from_bus] = y_bus_matrix[from_bus][to_bus]

    # Calculate sum of admittances connected to a bus
    # This is done in another step because it depends on the calculation above
    for i in range(bus_count):
        admittance_sum = 0
        for from_bus, to_bus, real, imag in line_data:
            if from_bus == i:
                admittance_sum += y_bus_matrix[i][to_bus]
            elif to_bus == i:
                admittance_sum += y_bus_matrix[i][from_bus]

        y_bus_matrix[i][i] = -1 * admittance_sum
    return y_bus_matrix


def calculate_q_for_pv_bus(bus_idx, bus_data, y_bus_matrix):
    v = complex(bus_data[bus_idx][3], bus_data[bus_idx][4])
    yv = complex(0, 0)
    for i in range(len(bus_data)):
        yv += y_bus_matrix[bus_idx][i] * complex(bus_data[i][3], bus_data[i][4])

    q = -1 * (v.conjugate() * yv).imag
    return q


def calculate_v(bus_idx, bus_data, y_bus_matrix):
    curr_v = complex(bus_data[bus_idx][3], bus_data[bus_idx][4])
    I = complex(bus_data[bus_idx][1], -1 * bus_data[bus_idx][2]) / curr_v.conjugate()

    yv = 0
    for n in range(len(bus_data)):
        if n != bus_idx:
            yv += y_bus_matrix[bus_idx][n] * complex(bus_data[n][3], bus_data[n][4])

    new_v = (I - yv) / y_bus_matrix[bus_idx][bus_idx]
    return new_v


def gauss_seidel(bus_data, y_bus_matrix):
    print("\n\nStarting Gauss-Seidel method!")
    iteration_count = 3
    for i in range(iteration_count):
        print(f"\nIteration {i+1}")
        for j in range(len(bus_data)):
            if bus_data[j][0] == 1:
                # Skip slack bus
                continue

            if bus_data[j][0] == 2:
                # Calculate Q value for PV bus
                q = calculate_q_for_pv_bus(j, bus_data, y_bus_matrix)

                # Update Q value for PV bus
                bus_data[j][2] = q

            # Calculate V value for the current iteration
            v = calculate_v(j, bus_data, y_bus_matrix)  # this is a complex number

            # Update V only for the PQ bus
            if bus_data[j][0] == 3:
                bus_data[j][3] = v.real

            # Update imaginary part for this bus
            bus_data[j][4] = v.imag
        print_bus_data(bus_data)
