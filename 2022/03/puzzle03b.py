# puzzle03b.py
import string

def main():
    input_file = open("input03.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    line_len = 0
    total_priorities = 0
    sacks = []
    GROUP_SIZE = 3

    for i in range(0, num_lines//GROUP_SIZE):
        for j in range(0, GROUP_SIZE):
            line = lines[i*GROUP_SIZE + j].strip()
            if j:
                sacks = list(set(sacks).intersection(set(list(line))))
            else:
                sacks = list(line)

        # print(sacks)
        common_char = sacks[0]
        if common_char in string.ascii_uppercase:
            priority = ord(common_char) - 64 + 26
        elif common_char in string.ascii_lowercase:
            priority = ord(common_char) - 96
        total_priorities += priority
        print(common_char, priority, total_priorities)

    print("Total priorities: {n}\n".format(n=total_priorities))
    # Answer: 2838

if __name__ == "__main__":
    main()
