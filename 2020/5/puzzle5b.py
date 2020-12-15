# puzzle5a.py

# For rows:
#   "B" (back) is binary 1
#   "F" (front) is binary 0
# For columns:
#   "L" (left) is binary 0
#   "R" (right) is binary 1

def main():
    boarding_passes = read_file()

    bp_dict = dict()

    for bp in boarding_passes:
        bp = bp.rstrip("\n")
        col = int(bp[:7].replace("B", "1").replace("F", "0"), 2)
        row = int(bp[-3:].replace("L", "0").replace("R", "1"), 2)
        seat_nbr = col * 8 + row
        bp_dict[seat_nbr] = bp

    sorted_keys = sorted(bp_dict.keys())
    my_boarding_pass = find_missing(sorted_keys)
    print("My boarding pass: " + str(my_boarding_pass))

def find_missing(_list):
    return [x for x in range(_list[0], _list[-1] + 1)
            if x not in _list]
            
def read_file():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    return lines

if __name__ == "__main__":
    main()