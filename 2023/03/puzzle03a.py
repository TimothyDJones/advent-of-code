# puzzle03a.py
import string
from pprint import pformat
import re

def main():
    input_file = open("input03.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    line_length = len(lines[0])
    valid_part_nums = list()
    symbols = {}

    for row in range(len(lines)):
        for col in range(len(lines[0]) - 1):
            if lines[row][col] not in "0123456789.":
                symbols[(row, col)] = lines[row][col]
                
    # print("{s}".format(s=pformat(object=symbols, indent=2)))
    
    for row_num, row in enumerate(lines):
        for a in re.finditer(r"\d+", row):
            valid = False
            viable_symbol_positions = list()
            for i in range(a.start() - 1, a.end() + 1):
                viable_symbol_positions.append(((row_num - 1), i))
                viable_symbol_positions.append((row_num, i))
                viable_symbol_positions.append(((row_num + 1), i))
            for v in viable_symbol_positions:
                if v in symbols:
                    valid = True
            if valid:
                valid_part_nums.append(int(a.group()))
                
    # print("{p}".format(p=pformat(object=valid_part_nums, indent=2)))
        
    print("Total of valid part numbers: {n}\n".format(n=sum(valid_part_nums)))
    # Answer: 544664

if __name__ == "__main__":
    main()