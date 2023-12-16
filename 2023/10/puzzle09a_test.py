from functools import reduce

# Input loading
with open("input09.txt", "r") as f:
    lines = [list(map(int, line.strip().split())) for line in f.readlines()]
    puzzle_input = lines

# Helper functions
def find_next_value(sequence):
    last_val = sequence[-1]
    last_vals = [last_val]
    while last_val:
        reduced_sequence = [y-x for x,y in list(zip(sequence[:-1], sequence[1:]))]
        last_val = reduced_sequence[-1]
        last_vals.append(last_val)
        sequence = reduced_sequence
    print(sum(last_vals))
    return sum(last_vals)

def find_prev_value(sequence):
    first_val = sequence[0]
    first_vals = [first_val]
    last_val = sequence[-1]
    last_vals = [last_val]
    while last_val:
        reduced_sequence = [y-x for x,y in list(zip(sequence[:-1], sequence[1:]))]
        first_val = reduced_sequence[0]
        first_vals.append(first_val)
        last_val = reduced_sequence[-1]
        last_vals.append(last_val)
        sequence = reduced_sequence
    first_vals = list(reversed(first_vals))
    predicted = reduce(lambda x,y: y-x, first_vals)
    return predicted

# Main functions
def day9_part1(puzzle_input):
    solution = 0
    for sequence in puzzle_input:
        solution += find_next_value(sequence)
    print("Part1 solution: " + str(solution))
    return solution

def day9_part2(puzzle_input):
    solution = 0
    for sequence in puzzle_input:
        solution += find_prev_value(sequence)
    print("Part2 solution: " + str(solution))
    return solution

# Tests
# if day9_part1(puzzle_input) == 114:
#     print("Part1 test: PASS")
# else:
#     print("Part1: FAIL")

# if day9_part2(puzzle_input) == 2:
#     print("Part2 test: PASS")
# else:
#     print("Part2: FAIL")

# Solutions
day9_part1(puzzle_input)

day9_part2(puzzle_input)