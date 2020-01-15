from src.d2q1 import run_intcode

input_data = [int(x) for x in open('../inputs/d2q1').read().split(',')]
print(f'hey hey hey {input_data}')
l = len(input_data)
print(l)

goal = 19690720

for x in range(l):
    for y in range(l):
        result = run_intcode(input_data, x, y)
        if result and result[0] == goal:
            print(x, y)
            print(100 * x + y)
            exit()

