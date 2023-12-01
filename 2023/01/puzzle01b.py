# puzzle01b.py
import string

OVERLAP_MAP = {
    "oneight": "oneeight",
    "threeight": "threeeight",
    "fiveeight": "fiveeight",
    "nineight": "nineeight",
    "twone": "twoone",
    "sevenine": "sevennine",
    "eightwo": "eighttwo"
}
LETTER_TO_NUMBER_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def main():
    input_file = open("input01b.txt", "r")
    # input_file = open("test.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    cal_code_list = list()
    total_cal_value = 0

    for line in lines:
        _line = line
        for k, v in OVERLAP_MAP.items():
            line = line.replace(k, v)
        for k, v in LETTER_TO_NUMBER_MAP.items():
            line = line.replace(k, v)
        cal_code = line.translate({ord(i): None for i in string.ascii_letters + "\n"})
        # print(_line, cal_code)
        # print(cal_code[0], cal_code[-1])
        cal_code = int(cal_code[0] + cal_code[-1])
        # print(cal_code)
        cal_code_list.append(cal_code)

    # print(len(cal_code_list))

    print("Total of calibration values: {n}\n".format(n=sum(cal_code_list)))
    # Answer: 54728

if __name__ == "__main__":
    main()