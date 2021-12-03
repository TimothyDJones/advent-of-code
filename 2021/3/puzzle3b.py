# puzzle3b.py
def get_rating(input_data, rating_type, num_len):

    def rating_type_compare(rating_type, count_0, count_1):
        if rating_type.upper() in ["OXYGEN", "O2"]:
            return (count_0 > count_1)
        elif rating_type.upper() in ["CO2"]:
            return (count_0 <= count_1)

    # Strategy: For each position in binary representation, extract the
    # digits (0 or 1) from each number (line of input). Count the number of 0s
    # and 1s for that position and determine which is greater (for oxygen)
    # smaller (for CO2) to determine which numbers from input to keep for
    # next iteration. If 0s and 1s are equal, keep based on 1s for oxygen
    # and 0s for CO2. Repeat/iterate for each position. Iterate twice: once for
    # oxygen and once for CO2.

    input_values = input_data        # Initial values are numbers from input file.
    for i in range(num_len):
        column = list()
        num_count = len(input_values)
        for j in range(num_count):
            num_digits = list(input_values[j])     # Expand binary number input into array of digits as characters
            column.append(num_digits[i])    # Take the digit character from the appropriate position

        # Get counts of 0s and 1s for this position
        count_0 = len([val for val in column if val == "0"])
        count_1 = len([val for val in column if val == "1"])

        # Determine values for next iteration
        if rating_type_compare(rating_type, count_0, count_1):
            input_values = [val for val in input_values
                            if list(val)[i] == "0"]
        else:
            input_values = [val for val in input_values
                            if list(val)[i] == "1"]

        if len(input_values) == 1:
            return (input_values[0])

def main():
    input_file = open("input3b.txt", "r")
    lines = input_file.read().splitlines()

    num_count = len(lines)      # Count of numbers in list
    num_len = len(lines[0])     # Length of each number in list

    (oxygen, co2) = ("", "")

    # Determine oxygen generator rating
    oxygen = get_rating(input_data=lines, rating_type="oxygen", num_len=num_len)

    # Determine CO2 scrubber rating
    co2 = get_rating(input_data=lines, rating_type="CO2", num_len=num_len)

    print("oxygen: {o}\nCO2: {c}\nProduct: {p}\n"
        .format(o=oxygen,
        c=co2,
        p=(int(oxygen, 2) * int(co2, 2))))

if __name__ == "__main__":
    main()