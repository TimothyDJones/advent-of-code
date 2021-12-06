# puzzle6a.py
from utils import *
from pprint import pprint, pformat

# Strategy:
# Iterate through list 80 times (80 days). For each item in list, check value.
# If value is 0, change the value to 6 and append a new value of 8 to the list.
# After 80 days, determine the length of the list, which is the number of fish.

def main():
    input_data = read_input_from_file(filename="input6a.txt", datatype=str,
        sep="\n")
    fish_list = list(map(int, input_data[0].split(",")))

    for day in range(1, 81):
        for i in range(len(fish_list)):
            if not fish_list[i]:
                fish_list[i] = 6
                fish_list.append(8)
            else:
                fish_list[i] -= 1

        print("After Day {d}: {l}".format(d=day, l=len(fish_list)))

    print("Number of fish after 80 days: {n}".format(n=len(fish_list)))

if __name__ == "__main__":
    main()