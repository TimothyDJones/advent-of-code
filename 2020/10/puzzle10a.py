# puzzle10a.py
import sys

def main():
    count_diff_1 = 0
    count_diff_3 = 0

    adapters = read_file()

    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i - 1]
        if diff == 1:
            count_diff_1 += 1
        elif diff == 3:
            count_diff_3 += 1

    result = count_diff_1 * count_diff_3

    print("Puzzle answer: " + str(result))

def read_file():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

        items = []
        for line in lines:
            items.append(int(line))

        # add implied values of 0 and maximum + 3
        items.append(0)
        items.append(max(items) + 3)

        # sort items in ascending order
        items = sorted(items)

        return items

if __name__ == "__main__":
    main()