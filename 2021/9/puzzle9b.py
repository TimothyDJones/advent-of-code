# puzzle8b.py
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

def check_adj_point(floor_table, r1, c1, r2, c2):
    # We assume (r1, c1) is a "relative" low point.
    # print(r1, c1, r2, c2, floor_table[r1][c1], floor_table[r2][c2])
    if floor_table[r2][c2] >= 9:
        return False
    else:
        return (floor_table[r1][c1] < floor_table[r2][c2])

def get_basin_size(floor_table, r, c):
    (basin, points_searched) = (set(), set())
    basin.add((r, c))

    # Recursively search floor map
    def search_basin(r, c):
        nonlocal basin, points_searched
        # print(basin, points_searched, (r, c))
        if (r, c) in points_searched: return    # Return if point already processed.

        to_search = set()   # Set of other points to search, recursively.
        for _dir in OFFSET:
            (x_a, y_a) = (r, c)
            (x_b, y_b) = (r + _dir[0], c + _dir[1])
            while check_adj_point(floor_table=floor_table, r1=x_a, c1=y_a,
                r2=x_b, c2=y_b):
                coord = (x_b, y_b)
                basin.add(coord)
                # print(basin, coord)
                if coord not in points_searched:
                    to_search.add(coord)

                # Move to next point
                (x_a, y_a) = (x_b, y_b)
                x_b += _dir[0]
                y_b += _dir[1]

            # Add point to list of points searched
            points_searched.add((r, c))

            # Search points added to list
            for point in to_search:
                search_basin(*point)

    # Recursively search basin
    search_basin(r, c)
    # print(basin, len(basin))
    return (len(basin))

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

    basin_sizes = list()
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if (check_low_point(floor_table=floor_table, r=r, c=c)):
                # For each low point, check the adjacent points for descending
                # series of adjacent points.
                basin_sizes.append(get_basin_size(floor_table, r, c))
    # print(basin_sizes)

    top_3_basins = list(sorted(basin_sizes, reverse=True))[:3]
    prod_top_3_basins = top_3_basins[0] * top_3_basins[1] * top_3_basins[2]

    print("Product of sizes of top 3 basins: {p}".format(
        p=prod_top_3_basins))

if __name__ == "__main__":
    main()