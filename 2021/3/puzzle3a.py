# puzzle3a.py
def main():
    input_file = open("input3a.txt", "r")
    lines = input_file.read().splitlines()

    # Strategy: Convert the list of binary numbers into arrays/lists of
    # digits for each position (0 - length of numbers). Count number of 0s
    # and 1s in each array/list to determine that position's value (0 or 1)
    # for gamma and epsilon.

    num_count = len(lines)      # Count of numbers in list
    num_len = len(lines[0])     # Length of each number in list

    # List/array of digits for each position for gamma and epsilon
    (gamma, epsilon) = (list(), list())

    for i in range(num_len):
        column = list()
        for j in range(num_count):
            num_digits = list(lines[j])     # Expand binary number input into array of digits as characters
            column.append(num_digits[i])    # Take the digit character from the appropriate position

        # Get counts of 0s and 1s for this position
        count_0 = len([val for val in column if val == "0"])
        count_1 = len([val for val in column if val == "1"])

        # Determine values for gamma and epsilon for this position
        if count_0 > count_1:
            gamma.append("0")
            epsilon.append("1")
        else:
            gamma.append("1")
            epsilon.append("0")

    print("gamma: {g}\nepsilon: {e}\nProduct: {p}\n"
        .format(g="".join(gamma),
        e="".join(epsilon),
        p=(int("".join(gamma), 2) * int("".join(epsilon), 2))))

if __name__ == "__main__":
    main()