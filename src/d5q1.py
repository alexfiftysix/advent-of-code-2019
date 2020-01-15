import enum


class ParameterMode(enum.Enum):
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1


class IntcodeComputer:
    def __init__(self, input_data):
        self.instructions = input_data.copy()
        self.position = 0
        self.INPUT = 1
        self.parameter_mode = ParameterMode.POSITION_MODE
        self.op_code = None
        self.operations = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            99: self.end
        }

    def run(self, input_data):
        # self.instructions = input_data.copy()
        # self.instructions[1] = 12
        # self.instructions[2] = 2
        while True:
            self.op_code = self.instructions[self.position]
            instruction = int(str(self.op_code)[-2:])
            print('*' * 50)
            print(f'instruction: {instruction}')
            operation = self.operations[instruction]
            operation()

    @staticmethod
    def get_parameter_modes(operation):
        operation = str(operation)[::-1]  # reverse
        operation = operation[2:]  # lose first 2 chars
        # print(operation)
        modes = [0, 0, 0]
        i = 0
        while len(operation) > 0:
            if i == 3:
                break
            modes[i] = int(operation[0])
            operation = operation[1:]
            i += 1

        return [ParameterMode(x) for x in modes]

    def add_or_mult(self, is_add=True):
        modes = IntcodeComputer.get_parameter_modes(self.op_code)

        a = self.instructions[self.position + 1]
        if modes[0] == ParameterMode.POSITION_MODE:
            a = self.instructions[a]

        b = self.instructions[self.position + 2]
        if modes[1] == ParameterMode.POSITION_MODE:
            b = self.instructions[b]

        write_position = self.instructions[self.position + 3]
        op = '+' if is_add else '*'
        print(f'{a} {op} {b} at position {write_position}')
        if is_add:
            self.instructions[write_position] = a + b
        else:
            self.instructions[write_position] = a * b

        self.position += 4

    def add(self):
        """ opcode 1 """
        self.add_or_mult(True)

    def multiply(self):
        """ opcode 2 """
        self.add_or_mult(False)

    def input(self):
        """ opcode 3 """
        write_position = self.instructions[self.position + 1]
        self.instructions[write_position] = self.INPUT
        self.position += 2

    def output(self):
        """ opcode 4 """
        modes = IntcodeComputer.get_parameter_modes(self.instructions[self.position])
        a = self.instructions[self.position + 1]
        if modes[0] == ParameterMode.POSITION_MODE:
            a = self.instructions[a]
        self.INPUT = a
        self.position += 2

    def jump(self, if_true=True):
        modes = IntcodeComputer.get_parameter_modes(self.instructions[self.position])

        a = self.instructions[self.position + 1]
        if modes[0] == ParameterMode.POSITION_MODE:
            a = self.instructions[a]

        if bool(a) and bool(if_true) or not bool(a) and not bool(if_true):
            b = self.instructions[self.position + 2]
            if modes[1] == ParameterMode.POSITION_MODE:
                b = self.instructions[b]
            self.position = b
        else:
            self.position += 3

    def jump_if_true(self):
        """ opcode 5 """
        self.jump(True)

    def jump_if_false(self):
        """ opcode 6 """
        self.jump(False)

    def less_than(self):
        """ opcode 7 """
        modes = IntcodeComputer.get_parameter_modes(self.instructions[self.position])

        a = self.instructions[self.position + 1]
        if modes[0] == ParameterMode.POSITION_MODE:
            a = self.instructions[a]

        b = self.instructions[self.position + 2]
        if modes[1] == ParameterMode.POSITION_MODE:
            b = self.instructions[b]

        write_to = self.instructions[self.position + 3]

        if a < b:
            self.instructions[write_to] = 1
        else:
            self.instructions[write_to] = 0

        self.position += 4

    def equals(self):
        """ opcode 8 """
        modes = IntcodeComputer.get_parameter_modes(self.instructions[self.position])

        a = self.instructions[self.position + 1]
        if modes[0] == ParameterMode.POSITION_MODE:
            a = self.instructions[a]

        b = self.instructions[self.position + 2]
        if modes[1] == ParameterMode.POSITION_MODE:
            b = self.instructions[b]

        write_to = self.instructions[self.position + 3]

        if a == b:
            self.instructions[write_to] = 1
        else:
            self.instructions[write_to] = 0

        self.position += 4

    def end(self):
        print(f'OUTPUT: {self.INPUT}')
        print(self.instructions)
        exit(0)


if __name__ == '__main__':
    input_data = [int(x) for x in open('../inputs/d5q1').read().split(',')]
    # input_data = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    computer = IntcodeComputer(input_data)
    computer.INPUT = 5
    print(computer.instructions)
    computer.run(input_data)
