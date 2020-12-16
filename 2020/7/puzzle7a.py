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
    
    @lru_cache(maxsize=256)
    def can_hold(in_color, out_color):
        if in_color in str(bags[out_color]):
            return True
        return any([can_hold(in_color, b) for b in bags[out_color]])

    bag_colors_count = sum([can_hold(BAG_COLOR, bag) for bag in bags])

    print("Bag colors holding " + BAG_COLOR + ": " + str(bag_colors_count))



if __name__ == "__main__":
    main()