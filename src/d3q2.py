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


class WirePoint:
    def __init__(self, x, y, distance_from_start):
        self.x = x
        self.y = y
        self.distance_from_start = distance_from_start

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return WirePoint(self.x + other.x, self.y + other.y, self.distance_from_start + other.distance_from_start)

    def distance(self, other):
        return self.distance_from_start + other.distance_from_start

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'{self.x},{self.y},{self.distance_from_start}'


class Wire:
    def __init__(self, instruction_list):
        self.instructions = [Instruction(x) for x in instruction_list.split(',')]

        directions = {
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1)
        }

        self.points = {}

        position = (0, 0)
        distance_from_start = 0
        for instruction in self.instructions:
            to_move = instruction.amount
            while to_move > 0:
                position = (
                    position[0] + directions[instruction.direction][0],
                    position[1] + directions[instruction.direction][1]
                )
                distance_from_start += 1
                self.points[position] = distance_from_start
                to_move -= 1

    def get_intersections(self, other):
        """other: Wire"""
        return set(self.points.keys()).intersection(set(other.points.keys()))


def find_closest_intersection(wire_1_instructions, wire_2_instructions):
    wire_1 = Wire(wire_1_instructions)
    wire_2 = Wire(wire_2_instructions)
    intersections = wire_1.get_intersections(wire_2)
    print(intersections)

    lowest_distance = math.inf
    for i in intersections:
        distance = wire_1.points[i] + wire_2.points[i]
        if distance < lowest_distance:
            lowest_distance = distance

    return lowest_distance


if __name__ == '__main__':
    instructions = open('../inputs/d3q1', 'r').readlines()
    print(find_closest_intersection(
        instructions[0], instructions[1]
    ))
