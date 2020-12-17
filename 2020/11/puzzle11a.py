# puzzle11a.py

import sys
from functools import lru_cache

# R = number of rows --> len(grid)
# C = number of colums --> len(grid[0])

def main():

    grid = read_file()

    R = len(grid)
    C = len(grid[0])
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                 (0, 1), (1, -1), (1, 0), (1, 1)]
    next_grid = [[grid[r][c] for c in range(C)] for r in range(R)]

    while True:
        changed = False
        for r in range(R):
            for c in range(C):
                occupied = 0
                for (x, y) in neighbors:
                    if (0 <= c + x < C) and (0 <= r + y < R):
                        if grid[r + y][c + x] == "#":
                            occupied += 1
                
                if grid[r][c] == "L" and occupied == 0:
                    next_grid[r][c] = "#"
                    changed = True
                elif grid[r][c] == "#" and occupied >= 4:
                    next_grid[r][c] = "L"
                    changed = True
                else:
                    next_grid[r][c] = grid[r][c]

        if not changed:
            break

        grid = [[next_grid[r][c] for c in range(C)] for r in range(R)]
    
    result = sum([sum([grid[r][c] == "#" for c in range(C)]) for r in range(R)])

    print("Seats occupied after no more changes: " + str(result))

def read_file():
    grid = []
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        for line in lines:
            grid.append(list(line.strip("\n")))

        return grid

if __name__ == "__main__":
    main()