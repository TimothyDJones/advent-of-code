# puzzle7b.py
from utils import *
from pprint import pprint, pformat

# Strategy:
# Find minimum and maximum values in list as boundaries for iteration.
# Iterate through list and build list/array of deltas (absolute value) for each
# position from that test position to determine the fuel spent. In this
# scenario, we observe that the fuel spent is (1 + 2 + 3 + ... + (n - 1) + n),
# where n is the number positions moved. We can take advantage of the fact
# that this series has closed form solution of (n * (n + 1)) / 2.
# Subsequently, we continue as before:
# Sum up those values for total fuel spent for that position. If the fuel spent
# is less than the current minimum, then keep this position and fuel spent as
# best choice.

def main():
    input_data = read_input_from_file(filename="input7b.txt", datatype=str,
        sep="\n")
    crab_pos = list(map(int, input_data[0].split(",")))
    (_min, _max) = (min(crab_pos), max(crab_pos))

    (best_pos, min_fuel_spent) = (0, 1000 * sum(crab_pos))

    for test_pos in range(_min, _max + 1):
        delta = list()
        for crab in crab_pos:
            pos_moved = abs(crab - test_pos)
            delta.append((pos_moved * (pos_moved + 1)) // 2)
        if sum(delta) < min_fuel_spent:
            (best_pos, min_fuel_spent) = (test_pos, sum(delta))

    print("Best position: {p}\nFuel spent: {f}\n".format(p=best_pos,
        f=min_fuel_spent))

if __name__ == "__main__":
    main()