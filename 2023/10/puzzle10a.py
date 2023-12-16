# puzzle10a.py
from pprint import pformat

NEXT_PIPE = {                  # (dx, dy)
    '|': {( 0,  1), ( 0, -1)}, # down, up
    '-': {( 1,  0), (-1,  0)}, # right, left
    'L': {( 0, -1), ( 1,  0)}, # up, right
    'J': {( 0, -1), (-1,  0)}, # up, left
    '7': {(-1,  0), ( 0,  1)}, # left, down
    'F': {( 0,  1), ( 1,  0)}, # down, right
}

def parse_data():
    input_file = open("input10.txt", "r")
    # input_file = open("test.txt", "r")
    # data = input_file.readlines()
    
    data_map = [list(line.strip()) for line in input_file.readlines()]

    print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map) 

def main():
    data = parse_data()
    
    distance = 0
    pipe_distance_map = dict()
    start = None
    
    for y, row in enumerate(data):
        if "S" in row:
            start = (row.index("S"), y)
            break
    print(start, data[start[1]][start[0]])
            
    # Consider "start" ("S") to be an "F" tile for purposes of traversing map.
    data[start[1]][start[0]] = "F"
    pipe = start
    while pipe not in pipe_distance_map:
        pipe_distance_map[pipe] = distance
        distance += 1
        
        x, y = pipe
        c = data[y][x]
        # print(x, y, pipe_distance_map)
        for dx, dy in NEXT_PIPE[c]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in pipe_distance_map:
                pipe = (nx, ny)
                break
    
    print("Steps to point farthest from start: {n}\n".format(n=(distance // 2)))
    # Answer: 18673

if __name__ == "__main__":
    main()