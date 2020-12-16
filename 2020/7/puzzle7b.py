# puzzle7a.py
# https://0xdf.gitlab.io/adventofcode2020/7

import sys
from collections import defaultdict     # Use defaultdict to avoid KeyError
from functools import lru_cache

def main():
    BAG_COLOR = "shiny gold"

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    bags = defaultdict(dict)

    for line in lines:
        parts = line.split(" ")
        color = " ".join(parts[:2])
        in_parts = " ".join(parts[4:]).split(",")
        for part in in_parts:
            if not "no other bags" in part:
                sp = part.strip().split(" ")
                bags[color][" ".join(sp[1:3])] = int(sp[0])
            else:
                bags[color] = {}
    
    def num_inside(color):
        return sum([bags[color][b] * (1 + num_inside(b)) for b in bags[color]])

    contained_bags = num_inside(BAG_COLOR)

    print("Bags inside " + BAG_COLOR + " bags: " + str(contained_bags))

if __name__ == "__main__":
    main()