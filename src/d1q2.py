def calculate_fuel_needed(mass):
    """Calculates fuel needed, and fuel needed for that fuel, and so on"""
    fuel_needed = mass // 3 - 2
    if fuel_needed <= 0:
        return 0
    return fuel_needed + calculate_fuel_needed(fuel_needed)


if __name__ == '__main__':
    file = open('../inputs/d1q1', 'r')
    inputs = [int(x) for x in file.readlines()]

    output = sum([calculate_fuel_needed(mass) for mass in inputs])
    out_file = open('../outputs/d1q2', 'w')
    out_file.write(str(output))
