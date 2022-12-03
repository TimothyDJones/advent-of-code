# puzzle03a.py
import string

def main():
    input_file = open("input03.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    line_len = 0
    total_priorities = 0
    comps = ["", ""]    # Compartments

    for i in range(0, num_lines):
        line = lines[i].strip()
        line_len = len(line)
        # print(line_len)
        comps = [line[0:line_len//2], line[line_len//2:]]
        common_char = list(set(list(comps[0])).intersection(
            set(list(comps[1]))))[0]
        if common_char in string.ascii_uppercase:
            priority = ord(common_char) - 64 + 26
        elif common_char in string.ascii_lowercase:
            priority = ord(common_char) - 96
        total_priorities += priority
        print(common_char, priority, total_priorities)

    print("Total priorities: {n}\n".format(n=total_priorities))
    # Answer: 7908

if __name__ == "__main__":
    main()
