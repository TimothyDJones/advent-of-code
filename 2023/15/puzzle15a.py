# puzzle15a.py
from pprint import pformat

MULT_CONST = 17

def parse_data():
    input_file = open("input15.txt", "r")
    # input_file = open("test.txt", "r")
    data = input_file.readlines()
    data_map = data[0].strip().split(",")

    # print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map) 

def hash(_input):
    hash_value = 0
    for c in list(_input):
        hash_value += ord(c)
        hash_value *= MULT_CONST
        hash_value %= 256
        # print(c, hash_value)
    
    return (hash_value)

def main():
    hash_map = dict()
    hash_total = 0
    data = parse_data()
    # data = ["HASH"]
    
    for item in data:
        # print(item)
        # hash_map[item] = hash(item)    
        hash_total += hash(item) 

    
    # print("hash_map: {s}".format(s=pformat(object=hash_map, indent=2)))
    print("Sum of hash results: {n}\n".format(n=hash_total))
    # Answer: 514639

if __name__ == "__main__":
    main()