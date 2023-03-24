from utility import print_matrix


def import_single_bus_data():
    single_bus_data = [0, 0, 0, 0, 0]

    print("------------------------")
    bus_type = int(input("Enter bus type: "))
    single_bus_data[0] = bus_type

    if bus_type == 2 or bus_type == 3:
        P = float(input("Enter P value: "))
        single_bus_data[1] = -1 * P

    if bus_type == 3:
        Q = float(input("Enter Q value: "))
        single_bus_data[2] = -1 * Q
        single_bus_data[3] = 1.0

    if bus_type == 1 or bus_type == 2:
        V = float(input("Enter V value: "))
        single_bus_data[3] = V

        DELTA = float(input("Enter delta value: "))
        single_bus_data[4] = DELTA
    return single_bus_data


def import_bus_data():
    print("========================")
    n = int(input("Enter number of buses: "))

    bus_data = []
    for i in range(n):
        print(f"\nBus number {i+1}:")
        bus_data.append(import_single_bus_data())
    print("========================")

    print("\nBus Data:")
    print_matrix(bus_data)
    return bus_data


def import_single_line_data():
    single_line_data = [0.0, 0.0, 0.0, 0.0]

    print("------------------------")
    from_bus = int(input("From bus number: "))
    # subtracting 1 because the user uses 1-based indices and Python arrays use 0-based indices
    single_line_data[0] = from_bus - 1

    to_bus = int(input("To bus number: "))
    # subtracting 1 because the user uses 1-based indices and Python arrays use 0-based indices
    single_line_data[1] = to_bus - 1

    real = float(input("Impedance (real part): "))
    single_line_data[2] = real

    imag = float(input("Impedance (imaginary part): "))
    single_line_data[3] = imag

    return single_line_data


def import_line_data():
    print("========================")
    n = int(input("Enter number of lines: "))

    line_data = []
    for i in range(n):
        print(f"\nLine number {i+1}:")
        line_data.append(import_single_line_data())
    print("========================")

    print("\nLine Data:")
    print_matrix(line_data)
    return line_data
