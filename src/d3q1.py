import math

# Example input
# R8,U5,L5,D3
# U7,R6,D4,L4
# Closest intersection distance = 6 (3+3)
# ...........
# .+-----+...
# .|.....|...
# .|..+--X-+.
# .|..|..|.|.
# .|.-X--+.|.
# .|..|....|.
# .|.......|.
# .o-------+.
# ...........


def manhattan_distance(a, b):
    """
    a: (x, y)
    b: (x, y)
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class Instruction:
    def __init__(self, s):
        """ s: instruction as string """
        self.direction = s[0]
        self.amount = int(s[1:])

    def __repr__(self):
        return f'{self.direction}|{self.amount}'


class Wire:
    def __init__(self, instruction_list):
        self.instructions = [Instruction(x) for x in instruction_list.split(',')]

        directions = {
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1)
        }

        self.points = set()

        position = (0, 0)
        for instruction in self.instructions:
            to_move = instruction.amount
            while to_move > 0:
                position = (position[0] + directions[instruction.direction][0], position[1] + directions[instruction.direction][1])
                self.points.add(position[:])
                to_move -= 1

    def get_intersections(self, other):
        """other: Wire"""
        return self.points.intersection(other.points)


def find_closest_intersection(wire_1_instructions, wire_2_instructions):
    wire_1 = Wire(wire_1_instructions)
    wire_2 = Wire(wire_2_instructions)
    intersections = wire_1.get_intersections(wire_2)
    print(intersections)

    lowest_distance = math.inf
    for i in intersections:
        distance = manhattan_distance((0,0), i)
        if distance < lowest_distance:
            lowest_distance = distance

    return lowest_distance


if __name__ == '__main__':
    instructions = open('../inputs/d3q1', 'r').readlines()
    print(find_closest_intersection(instructions[0], instructions[1]))
