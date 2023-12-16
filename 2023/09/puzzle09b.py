# puzzle08b.py
from pprint import pformat
import math

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
    
def find_nodes_ending_in_X(end_char, nodes):
    node_list = list()
    # print(nodes)
    for k, v in nodes.items():
        if k[-1] == end_char:
            node_list.append(k)
            
    return (node_list)

def lcm(_list):
    lcm = 1
    for i in _list:
        lcm = (lcm * i) // math.gcd(lcm, i)
        
    return (lcm)

def main():
    data = parse_data()
    
    start_nodes = find_nodes_ending_in_X(end_char="A", nodes=data[1])
    end_nodes = find_nodes_ending_in_X(end_char="Z", nodes=data[1])
    print("{s}\n{e}".format(s=pformat(object=start_nodes, indent=2), 
        e=pformat(object=end_nodes, indent=2)))
        
    move_count_list = list()
    
    for node in start_nodes:
        done = False
        move_count = 0
        curr_node = node
        while not done:
            for _dir in list(data[0]):
                move_count += 1
                if _dir == "L":
                    curr_node = data[1][curr_node][0]
                elif _dir == "R":
                    curr_node = data[1][curr_node][1]
                if curr_node in end_nodes:
                    done = True
                    break
                    
        move_count_list.append(move_count)
    
    print("Total steps from nodes ending in 'A' to nodes ending in 'Z': {n}\n".format(n=lcm(move_count_list)))
    # Answer: 17972669116327

if __name__ == "__main__":
    main()