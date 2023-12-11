# puzzle11a.py
from itertools import combinations
from pprint import pformat

def parse_data():
    input_file = open("input11.txt", "r")
    # input_file = open("test.txt", "r")
    data = input_file.readlines()
    data_map = [list(line.strip("\n")) for line in data]

    # print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map) 
    
def expand_grid(grid_data):
    new_row_data = list()
    new_grid_data = [[]]
    for row in grid_data:
        if len(set(row)) == 1:
            new_row_data.append(row)
            new_row_data.append(row)
        else:
            new_row_data.append(row)
    # print("{d}".format(d=pformat(object=new_row_data, indent=2)))
    
    cols = list()
    for i in range(len(new_row_data[0])):
        col = list()
        for j in range(len(new_row_data)):
            col.append(new_row_data[j][i])
        if len(set(col)) == 1:
            cols.append(col)
            cols.append(col)
        else:
            cols.append(col)
            
    rows = list()
    for i in range(len(cols[0])):
        row = list()
        for j in range(len(cols)):
            row.append(cols[j][i])
        rows.append(row)
            
    # print("{d}".format(d=pformat(object=rows, indent=2)))                     
    
    return (rows)    

def get_galaxy_coordinates(grid):
    print(grid)
    galaxy_coord = list()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # print(col, row, grid[row][col])
            if grid[row][col] == "#":
                galaxy_coord.append([col, row])
                
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
    grid = expand_grid(data)
    galaxy_coord = get_galaxy_coordinates(grid)
    pair_distances = find_distances_between_pairs(galaxy_coord)
    
    print("Sum of steps between all {p} pairs of galaxies: {n}\n".format(n=sum(pair_distances), p=len(pair_distances)))
    # Answer: 9556712

if __name__ == "__main__":
    main()