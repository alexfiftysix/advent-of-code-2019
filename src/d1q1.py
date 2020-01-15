def calculate_fuel_needed(mass):
    return mass // 3 - 2


if __name__ == '__main__':
    file = open('../inputs/d1q1', 'r')
    inputs = [int(x) for x in file.readlines()]

    output = sum([calculate_fuel_needed(mass) for mass in inputs])
    out_file = open('../outputs/d1q1', 'w')
    out_file.write(str(output))
