
def run_intcode(input_data, a=12, b=2):
    # 1202 alarm reset
    operations = input_data.copy()
    operations[1] = a
    operations[2] = b

    # print(f'start: {input_data}')

    opcodes = {
        1: 'add',
        2: 'multiply',
        99: 'end'
    }

    i = 0

    while True:
        instruction = opcodes.get(operations[i])
        if instruction == 'end':
            # TODO: Write output to file
            print('end!')
            print(operations)
            return operations
        elif instruction == 'add' or instruction == 'multiply':
            a = operations[operations[i + 1]]
            b = operations[operations[i + 2]]
            if a is None or b is None:
                print(f'bad index')
                return
            if instruction == 'add':
                operations[operations[i + 3]] = a + b
            elif instruction == 'multiply':
                operations[operations[i + 3]] = a * b
        else:
            # print(f"Bad instruction {input_data[i]}")
            return
        i += 4
