# puzzle8a.py
from utils import *
from pprint import pprint, pformat

# Strategy:
# Read in data as sets of ordered pairs starting with (0, 0) in the upper left
# corner structured as list of list of rows.
# Walk through data and compare value to each adjacent point. For points
# on border, use value of 10 for "dummy" points outside of map to ensure value
# under test is always less than it.
# For each low point found, calculate risk level as its value plus 1 and add
# it to total risk level.

OFFSET = [[0, -1],      # left
            [0, 1],     # right
            [-1, 0],    # up
            [1, 0]]     # down

def check_low_point(floor_table, r, c):
    (left, right, up, down) = (False, False, False, False)
    # print(r, c, floor_table[r][c], floor_table[r][c - 1], floor_table[r][c + 1], floor_table[r - 1][c], floor_table[r + 1][c])
    left = floor_table[r][c] < floor_table[r + OFFSET[0][0]][c + OFFSET[0][1]]
    right = floor_table[r][c] < floor_table[r + OFFSET[1][0]][c + OFFSET[1][1]]
    up = floor_table[r][c] < floor_table[r + OFFSET[2][0]][c + OFFSET[2][1]]
    down = floor_table[r][c] < floor_table[r + OFFSET[3][0]][c + OFFSET[3][1]]
    return (left and right and up and down)

def main():
    input_data = read_input_from_file(filename="input9a.txt", datatype=str,
        sep="\n")
    floor_table = list(map(nums, input_data))
    (rows, cols) = len(floor_table), len(floor_table[0])

    # Add "border" around input data with values of 10 to prevent index errors
    # when comparing edge values.
    tmp_floor_table = list()
    tmp_floor_table.append([10] * (cols + 2))
    for r in range(rows):
        row = list()
        row = [10] + floor_table[r] + [10]
        tmp_floor_table.append(row)
    tmp_floor_table.append([10] * (cols + 2))
    floor_table = tmp_floor_table
    # print(floor_table)

    total_risk_level = 0

    # Use starting index of 1, because of "border" values added above.
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if (check_low_point(floor_table=floor_table, r=r, c=c)):
                print("Low point: ({x}, {y}): {v}".format(x=r, y=c,
                    v=floor_table[r][c]))
                total_risk_level += (floor_table[r][c] + 1)

    print("Total risk level: {n}".format(n=total_risk_level))

if __name__ == "__main__":
    main()