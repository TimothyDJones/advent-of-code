# puzzle6b.py
from utils import *
from pprint import pprint, pformat

# Strategy:
# Due to performance considerations the strategy from part 1 doesn't work for
# part 2. So we must take a different approach.
# Consider that fish can be in one of 9 possible "states": 0, 1, 2, ..., 7, 8.
# On each iteration, we simply need to count the number of fish in each state
# and then process them accordingly. We can use a **list** where the index
# represents the "state" and the value represents the number/count of fish
# in that state for the given day (iteration).

def solve(fish_list, num_days):
    for day in range(1, (num_days + 1)):
        # Count number of 0 for this day.
        num_zero = fish_list[0]
        # Shift other values to left.
        # Spawn new fish in state 8 (index -1) for each fish in state 0
        fish_list = fish_list[1:] + [num_zero]
        # Reset each fish in state 0 to state 6.
        # (Note: Must **add** to any fish already in state 6.)
        fish_list[6] += num_zero

        print("After day {d}: {l}".format(d=day, l=fish_list))

    return (sum(fish_list))

def main():
    input_data = read_input_from_file(filename="input6a.txt", datatype=str,
        sep="\n")
    print(input_data)
    input_list = list(map(int, input_data[0].split(",")))

    # Populate dictionary with initial values from input data
    fish_list = [0] * 9
    for val in input_list:
        fish_list[val] += 1

    print(fish_list)

    print("Number of fish after {d} days: {n}"
        .format(d=80, n=solve(fish_list=fish_list, num_days=80)))
    print("Number of fish after {d} days: {n}"
        .format(d=256, n=solve(fish_list=fish_list, num_days=256)))

if __name__ == "__main__":
    main()