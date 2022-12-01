# puzzle01b.py
def main():
    input_file = open("input01b.txt", "r")
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

    # Find "top 3" elves: the 3 with with most calories.
    # Sort list and take slice of last values and sum values.

    print("Calories from 'top 3' elves: {n}\n".format(n=sum(sorted(elf)[-3:])))
    # Answer: 200945

if __name__ == "__main__":
    main()