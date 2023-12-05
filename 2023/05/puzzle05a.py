# puzzle05a.py
import string
from pprint import pformat
import re

def parse_data():
    input_file = open("input05.txt", "r")
    # input_file = open("test.txt", "r")
    data = input_file.read()
    data_list = [section.split(":") for section in data.split("\n\n")]
    
    data_map = dict()
    for section in data_list:
        data_map[section[0].replace(" map", "")] = \
            [line.split() for line in section[1].strip().split("\n")]
    print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map)
    
def check_conversion_map(value, conversion_map):
    """ 
    Takes the provided `conversion_map` and checks `value` to find
    it either in one of the map ranges or return the value itself, 
    if not found.
    """
    for line in conversion_map:
        if (int(value) >= int(line[1])
            and int(value) < (int(line[1]) + int(line[2]))):
            return (int(line[0]) + (int(value) - int(line[1])))
            
    return int(value)


def main():
    data = parse_data()
    
    lowest_location = None
    
    for seed in data["seeds"][0]:
        current_soil = seed
        for cm in data.keys():
            if not cm == "seeds":
                # print("{cm}".format(cm=cm))
                current_soil = check_conversion_map(current_soil, data[cm])
        print("Seed: {seed}, Location: {loc}".format(seed=seed, loc=current_soil))
        if not lowest_location or int(current_soil) < lowest_location:
            lowest_location = int(current_soil)
        
    print("Lowest location number is: {n}\n".format(n=lowest_location))
    # Answer: 324724204

if __name__ == "__main__":
    main()