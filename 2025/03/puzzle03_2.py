NUM_DIGITS = 12

def main():
    sum_max_joltages = 0

    with open("input03.txt", "r") as f:
        data = [list(map(int, list(line.strip()))) for line in f.readlines()]
        # print(data[0])

    for array in data:
        max_joltage = find_max_number_from_array(array=array)
        print("\t", max_joltage)
        sum_max_joltages += max_joltage

    print("Sum of maximum joltages: {j}".format(j=sum_max_joltages))

def find_max_number_from_array(array: list):
    # print(len(array), array)
    num_array = list()

    for i in range(NUM_DIGITS - 1, -1, -1):
        # print("\t", array, array[:-i], i, -i)
        _max = max(array[:-i]) if i != 0 else max(array)
        num_array.append(_max)
        array = array[(array.index(_max) + 1):]

    return int("".join(list(map(str, num_array))))

if __name__ == "__main__":
    main()
