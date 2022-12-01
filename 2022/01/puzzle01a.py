# puzzle01a.py
def main():
    input_file = open("input01a.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    elf = list()
    calories = 0

    for i in range(1, num_lines):
        if not lines[i] or lines[i] in ["\n"]:
            elf.append(calories)
            calories = 0
        else:
            calories += int(lines[i])

    print("Maximum calories: {n}\n".format(n=max(elf)))
    # Answer: 69693

if __name__ == "__main__":
    main()