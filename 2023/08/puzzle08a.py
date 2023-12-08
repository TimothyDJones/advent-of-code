# puzzle08a.py
from pprint import pformat

START_NODE = "AAA"
END_NODE = "ZZZ"

def parse_data():
    input_file = open("input08.txt", "r")
    # input_file = open("test.txt", "r")
    data = input_file.read()
    data_list = [section for section in data.split("\n\n")]

    data_map = list()
    node_map = dict()
    
    for line in [line for line in data_list[1].strip().split("\n")]:
        label, coord = line.split(" = ")
        left, right = coord[1:-1].split(", ")
        node_map[label] = [left, right]
        
    data_map.append(data_list[0])
    data_map.append(node_map)

    # print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map) 

def main():
    data = parse_data()
    
    done = False
    move_count = 0
    curr_node = START_NODE
    while not done:
        for _dir in list(data[0]):
            move_count += 1
            if _dir == "L":
                curr_node = data[1][curr_node][0]
            elif _dir == "R":
                curr_node = data[1][curr_node][1]
            if curr_node == END_NODE:
                done = True
                break
    
    print("Total steps from AAA to ZZZ: {n}\n".format(n=move_count))
    # Answer: 18673

if __name__ == "__main__":
    main()