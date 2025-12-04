

def main():
    sum_max_joltages = 0

    with open("input03.txt", "r") as f:
        data = [list(map(int, list(line.strip()))) for line in f.readlines()]
        # print(data[0])

    for array in data:
        max_joltage = find_max_two_digit_number_from_array(array=array)
        # print("\t", max_joltage)
        sum_max_joltages += max_joltage

    print("Sum of maximum joltages: {j}".format(j=sum_max_joltages))

def find_max_two_digit_number_from_array(array: list):
    _max = 0
    for index, item in enumerate(array):
        for n in array[(index + 1):]:
            if int(str(item) + str(n)) > _max:
                _max = int(str(item) + str(n))
            
    return _max

if __name__ == "__main__":
    main()
