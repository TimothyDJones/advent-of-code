# puzzle2a.py
def main():
    valid_password_count = 0

    input_file = open("input.txt", "r")
    lines = input_file.readlines()
    for line in lines:
        if check_password(parse_line(line)):
            valid_password_count += 1

    print("Valid passwords: " + str(valid_password_count))         


def check_password(check_dict):
    # XOR the check of character at each position
    if (check_dict["password"][int(check_dict["min"]) - 1] == check_dict["char"]) \
        ^ (check_dict["password"][int(check_dict["max"]) - 1] == check_dict["char"]):
        return True
    
    return False

def parse_line(line):
    elems = line.split()
    _min = elems[0].split("-", 1)[0]
    _max = elems[0].split("-", 1)[1]
    char = elems[1][0]
    password = elems[2]

    return {"password": password,
        "min": _min,
        "max": _max,
        "char": char}



if __name__ == "__main__":
    main()