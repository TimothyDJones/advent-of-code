# puzzle12a.py

import sys
from math import cos, sin, radians

# R = number of rows --> len(grid)
# C = number of colums --> len(grid[0])

def main():

    instr = read_file()

    curr_dir = 90   # East
    (x, y) = (0, 0)

    for i in instr:
        if i["action"] == "N":
            y += i["mag"]
        elif i["action"] == "S":
            y -= i["mag"]
        elif i["action"] == "E":
            x += i["mag"]
        elif i["action"] == "W":
            x -= i["mag"]
        elif i["action"] == "L":
            curr_dir = (curr_dir - i["mag"]) % 360
        elif i["action"] == "R":
            curr_dir = (curr_dir + i["mag"]) % 360
        elif i["action"] == "F":
            x += round(sin(radians(curr_dir)) * i["mag"])
            y += round(cos(radians(curr_dir)) * i["mag"])

    result = (abs(x) + abs(y))

    print("Manhattan distance: " + str(result))

def read_file():
    instr = []
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        for line in lines:
            instr.append({"action": line[0], "mag": int(line[1:])})

        return instr

if __name__ == "__main__":
    main()