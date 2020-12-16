# puzzle9b.py
import sys

def main():
    TARGET_VAL = 15353384       # From puzzle 9a
    nums = read_file()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if sum(nums[i:j]) == TARGET_VAL:
                result = min(nums[i:j]) + max(nums[i:j])
                print("Sum of minimum and maximum adding to " + str(TARGET_VAL) +
                        ": " + str(result))
                sys.exit()

def read_file():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

        items = []
        for line in lines:
            items.append(int(line))
    
        return items

if __name__ == "__main__":
    main()