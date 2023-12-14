# puzzle11a.py
from functools import lru_cache
from pprint import pformat

def parse_data():
    input_file = open("input12.txt", "r")
    # input_file = open("test.txt", "r")
    data = input_file.readlines()
    
    data_map = list()
    for line in data:
        conditions, groups = line.split(" ")
        groups = tuple(map(int, groups.split(",")))
        data_map.append((conditions, groups))

    print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map) 
   
@lru_cache(maxsize=None)   
def count_arrangements(conditions, groups, next_is_lava):
    tr = lambda t: (t[0] - 1,) + t[1:]
    if not groups:
        return 0 if "#" in conditions else 1
    elif not conditions:
        return 0 if sum(groups) else 1
    elif groups[0] == 0:
        return count_arrangements(conditions[1:], groups[1:], False) if conditions[0] in ["?", "."] else 0
    elif next_is_lava:
        return count_arrangements(conditions[1:], tr(groups), True) if conditions[0] in ["?", "#"] else 0
    elif conditions[0] == "#":
        return count_arrangements(conditions[1:], tr(groups), True)
    elif conditions[0] == ".":
        return count_arrangements(conditions[1:], groups, False)
    else:
        return count_arrangements(conditions[1:], groups, False) + count_arrangements(conditions[1:], tr(groups), True)

@lru_cache(maxsize=None)
def arr_cnt(m, s, n):
    # m = measurement ("#?.#"), s = survey (1,2,3), n = is next spot lava
    tr = lambda t: (t[0] - 1,) + t[1:]  # lru_cache demands tuples
    if not s:
        return 0 if "#" in m else 1
    elif not m:
        return 0 if sum(s) else 1
    elif s[0] == 0:
        return arr_cnt(m[1:], s[1:], False) if m[0] in ["?", "."] else 0
    elif n:
        return arr_cnt(m[1:], tr(s), True) if m[0] in ["?", "#"] else 0
    elif m[0] == "#":
        return arr_cnt(m[1:], tr(s), True)
    elif m[0] == ".":
        return arr_cnt(m[1:], s, False)
    else:
        return arr_cnt(m[1:], s, False) + arr_cnt(m[1:], tr(s), True)

def main():
    possible_arrangements = list()
    data = parse_data()
    for conditions, groups in data:
        # possible_arrangements.append(count_arrangements(conditions, groups, False))
        possible_arrangements.append(arr_cnt(conditions, groups, False))
    
    print("Sum of possible arrangements: {n}\n".format(n=sum(possible_arrangements)))
    # Answer: 9556712

if __name__ == "__main__":
    main()