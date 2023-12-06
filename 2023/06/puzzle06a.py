# puzzle06a.py
import string
from pprint import pformat
import re

def parse_data():
    input_file = open("input06.txt", "r")
    # input_file = open("test.txt", "r")
    lines = input_file.readlines()
    _, times = lines[0].split(":")
    times = [int(t) for t in times.split()]
    _, distances = lines[1].split(":")
    distances = [int(d) for d in distances.split()]
    data_map = list(zip(times, distances))
    # print(times, distances)

    # print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map)


def main():
    data = parse_data()
    
    winning_combinations = list()
    result = 1
    
    for r in data:
        winners = 0
        for speed in range(1, r[0] - 1):
            dist = speed * (r[0] - speed)
            # print(r[0], r[1], "-->", speed, dist)
            if dist > r[1]:
                winners += 1
        # print(r[0], r[1], winners)
        winning_combinations.append(winners)
    
    for w in winning_combinations:
        result *= w
    print("Number of ways to win multiplied together: {n}\n".format(n=result))
    # Answer: 1084752

if __name__ == "__main__":
    main()