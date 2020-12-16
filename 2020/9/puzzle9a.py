# puzzle9a.py

def main():
    PREAMBLE_LEN = 25
    nums = read_file()

    index = PREAMBLE_LEN
    while True:
        if not is_valid_num(nums[index],
                nums[(index - PREAMBLE_LEN):index]):
            break

        index += 1

    print("First invalid number: " + str(nums[index]))

def is_valid_num(num, _list):
    while _list:
        n = _list.pop()
        diff = num - n
        if diff in _list:
            return True

    return False

def read_file():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

        items = []
        for line in lines:
            items.append(int(line))
    
        return items

if __name__ == "__main__":
    main()