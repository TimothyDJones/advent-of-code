# puzzle03b.py
import string
from pprint import pformat
import re

def main():
    input_file = open("input03.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    line_length = len(lines[0])
    gear_ratios = list()
    gears = dict()

    for row in range(len(lines)):
        for col in range(len(lines[0]) - 1):
            if lines[row][col] in "*":
                gears[(row, col)] = []
                
    # print("{s}".format(s=pformat(object=gears, indent=2)))
    
    for row_num, row in enumerate(lines):
        for a in re.finditer(r"\d+", row):
            valid = False
            viable_symbol_positions = list()
            for i in range(a.start() - 1, a.end() + 1):
                viable_symbol_positions.append(((row_num - 1), i))
                viable_symbol_positions.append((row_num, i))
                viable_symbol_positions.append(((row_num + 1), i))
            for v in viable_symbol_positions:
                if v in gears:
                    gears[v].append(int(a.group()))

    for g in gears:
        print(g, gears[g])
        if len(gears[g]) == 2:
            gear_ratios.append(gears[g][0] * gears[g][1])
                
    # print("{p}".format(p=pformat(object=valid_part_nums, indent=2)))
        
    print("Total of gear_ratios: {n}\n".format(n=sum(gear_ratios)))
    # Answer: 84495585

if __name__ == "__main__":
    main()