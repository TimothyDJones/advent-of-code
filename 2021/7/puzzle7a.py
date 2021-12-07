# puzzle7a.py
from utils import *
from pprint import pprint, pformat

# Strategy:
# Find minimum and maximum values in list as boundaries for iteration.
# Iterate through list and build list/array of deltas (absolute value) for each
# position from that test position to determine the fuel spent and then sum
# up those values for total fuel spent for that position. If the fuel spent
# is less than the current minimum, then keep this position and fuel spent as
# best choice.

def main():
    input_data = read_input_from_file(filename="input7a.txt", datatype=str,
        sep="\n")
    crab_pos = list(map(int, input_data[0].split(",")))
    (_min, _max) = (min(crab_pos), max(crab_pos))

    (best_pos, min_fuel_spent) = (0, sum(crab_pos))

    for test_pos in range(_min, _max + 1):
        delta = list()
        for crab in crab_pos:
            delta.append(abs(crab - test_pos))
        if sum(delta) < min_fuel_spent:
            (best_pos, min_fuel_spent) = (test_pos, sum(delta))

    print("Best position: {p}\nFuel spent: {f}\n".format(p=best_pos,
        f=min_fuel_spent))

if __name__ == "__main__":
    main()