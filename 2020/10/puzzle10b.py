# puzzle10b.py
# https://0xdf.gitlab.io/adventofcode2020/10
import sys
from functools import lru_cache

def main():

    adapters = read_file()

    # Find all paths (combinations) recursively in which
    # all differences in "joltage" between adapters is less
    # then or equal to 3.
    @lru_cache(maxsize=256)
    def paths_to_end(i):
        if i == len(adapters) - 1:
            return 1
        
        return sum(
            [
                paths_to_end(j)
                for j in range(i + 1, min(i + 4, len(adapters)))
                if (adapters[j] - adapters[i]) <= 3
            ]
        )

    result = paths_to_end(0)

    print("Puzzle answer: " + str(result))

def read_file():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

        items = []
        for line in lines:
            items.append(int(line))

        # add implied values of 0 and maximum + 3
        items.append(0)
        items.append(max(items) + 3)

        # sort items in ascending order
        items = sorted(items)

        return items

if __name__ == "__main__":
    main()