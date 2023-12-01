# puzzle01a.py
import string

def main():
    input_file = open("input01a.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    cal_code_list = list()
    total_cal_value = 0

    for line in lines:
        cal_code = line.translate({ord(i): None for i in string.ascii_letters + "\n"})
        # print(line, cal_code)
        # print(cal_code[0], cal_code[-1])
        cal_code = int(cal_code[0] + cal_code[-1])
        # print(cal_code)
        cal_code_list.append(cal_code)

    print("Total of calibration values: {n}\n".format(n=sum(cal_code_list)))
    # Answer: 54916

if __name__ == "__main__":
    main()