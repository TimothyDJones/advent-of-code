# puzzle4b.py
import re

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

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if not check_year(passport_dict["byr"], 1920, 2002):
            return False
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if not check_year(passport_dict["iyr"], 2010, 2020):
            return False
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if not check_year(passport_dict["eyr"], 2020, 2030):
            return False
        # hgt (Height) - a number followed by either cm or in:
        #   If cm, the number must be at least 150 and at most 193.
        #   If in, the number must be at least 59 and at most 76.
        if passport_dict["hgt"][-2:] == "cm":
            if not check_year(passport_dict["hgt"][:-2], 150, 193):
                return False
        elif passport_dict["hgt"][-2:] == "in":
            if not check_year(passport_dict["hgt"][:-2], 59, 76):
                return False
        else:
            return False
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        # Use regex to check for hex color string
        re_pattern = "^#([a-fA-F0-9]{6})$"
        if not re.match(re_pattern, passport_dict["hcl"]):
            return False
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if not (passport_dict["ecl"] in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])):
            return False
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        re_pattern = "^([0-9]{9})$"
        if not re.match(re_pattern, passport_dict["pid"]):
            return False
        # cid (Country ID) - ignored, missing or not.

        return True

    return False

def check_year(year, _min, _max):
    try:
        v = int(year)
        if not (v >= _min and v <= _max):
            return False
    except Exception:
        return False

    return True
            
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