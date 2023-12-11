# puzzle11b.py
from itertools import combinations
from pprint import pformat

EXPANSION_CONSTANT = 1000000

def parse_data():
    input_file = open("input11.txt", "r")
    # input_file = open("test.txt", "r")
    data = input_file.readlines()
    data_map = [list(line.strip("\n")) for line in data]

    # print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map) 
    
def expand_grid(grid_data):
    expanded_rows = list()
    for ridx, row in enumerate(grid_data):
        if len(set(row)) == 1:
            expanded_rows.append(ridx)
    # print("{d}".format(d=pformat(object=new_row_data, indent=2)))
    
    expanded_cols = list()
    for i in range(len(grid_data[0])):
        col = list()
        for j in range(len(grid_data)):
            col.append(grid_data[j][i])
        if len(set(col)) == 1:
            expanded_cols.append(i)
    # print(expanded_rows, expanded_cols)    
    # print("{d}".format(d=pformat(object=rows, indent=2)))                     
    
    return (expanded_rows, expanded_cols)    

def get_galaxy_coordinates(grid, expanded_rows, expanded_cols):
    print(grid)
    galaxy_coord = list()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # print(col, row, grid[row][col])
            if grid[row][col] == "#":
                new_col, new_row = col, row
                for r in expanded_rows:
                    if r < row:
                        new_row += EXPANSION_CONSTANT - 1
                for c in expanded_cols:
                    if c < col:
                        new_col += EXPANSION_CONSTANT - 1
                galaxy_coord.append([new_col, new_row])
    print(galaxy_coord)    
    return (galaxy_coord)

def find_distances_between_pairs(coordinates):
    distances = list()
    pairs = list(combinations(coordinates, 2))
    for pair in pairs:
        distance = (abs(pair[0][0] - pair[1][0])
            + abs(pair[0][1] - pair[1][1]))
        distances.append(distance)
        
    return (distances)
    

def main():
    data = parse_data()
    expanded_rows, expanded_cols = expand_grid(data)
    galaxy_coord = get_galaxy_coordinates(data, expanded_rows, expanded_cols)
    pair_distances = find_distances_between_pairs(galaxy_coord)
    
    print("Sum of steps between all {p} pairs of galaxies: {n}\n".format(n=sum(pair_distances), p=len(pair_distances)))
    # Answer: 678626199476

if __name__ == "__main__":
    main()