# puzzle4a.py
def main():
    passports = read_file()

    passport_count = 0
    valid_passport_count = 0
    for passport in passports:
        passport_count += 1
        if check_valid_passport(passport):
            valid_passport_count += 1
    
    print("Valid passports: " + str(valid_passport_count) +
        " [" + str(passport_count) + "]")

def check_valid_passport(passport_dict):
    required_keys = set(["byr", "iyr", "eyr",
        "hgt", "hcl", "ecl", "pid"])  # 'cid' is optional
    
    #if len(list(passport_dict.keys())) < 8:
    #    print(str(len(list(passport_dict.keys()))), passport_dict)
        
    if all(elem in passport_dict.keys() for elem in required_keys):
        return True

    return False

def read_file():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    new_lines = []
    new_lines.append("")
    new_lines_index = 0
    for line in lines:
        if len(line.rstrip("\n")) > 0:
            new_lines[new_lines_index] += " " + line.rstrip("\n")
        else:
            new_lines[new_lines_index] = new_lines[new_lines_index].strip()
            new_lines_index += 1
            new_lines.append("")

    passports = []
    for line in new_lines:
        d = dict(x.split(":") for x in line.split())
        #print(d)
        passports.append(d)
    
    return passports

if __name__ == "__main__":
    main()