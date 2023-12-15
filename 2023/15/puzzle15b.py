# puzzle15b.py
from pprint import pformat

MULT_CONST = 17

def parse_data():
    # input_file = open("input15.txt", "r")
    input_file = open("test.txt", "r")
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
    boxes = dict()
    data = parse_data()
    # data = ["HASH"]
    
    for item in data:
        box = hash(item)
        print(item, "=" in item)
        if "=" in item:
            label, focal_length = item.split("=")
            if boxes.get("box"):
                new_box = list()
                for k, v in boxes[box].items():
                    if k == label:
                        new_box(append({label: focal_length}))
                    else:
                        new_box(append({k: v}))
                boxes[box] = new_box
            else:
                boxes[box] = [{label: focal_length}]
        else:
            label = item[:-1]
            if boxes.get("box"):
                _box = boxes[box]
                for k, v in _box.items():
                    if k == label:
                        idx = _box.index({k, v})
                        del _box[idx]
                        break
                boxes[box] = _box
        
        print("boxes: {s}".format(s=pformat(object=boxes, indent=2)))
        # print(item)
        # hash_map[item] = hash(item)    

    
    # print("hash_map: {s}".format(s=pformat(object=hash_map, indent=2)))
    # print("Sum of hash results: {n}\n".format(n=hash_total))
    # Answer: 514639

if __name__ == "__main__":
    main()