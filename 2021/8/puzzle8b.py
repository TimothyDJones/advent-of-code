# puzzle8a.py
from utils import *
from pprint import pprint, pformat

# Strategy:
# Since 1, 4, 7, and 8 each have a unique number of segments (2, 4, 3, and 7,
# respectively), we can find the count of these directly from the output.
# We use a list to store the relevant information. The index of the list is
# the number of segments used, which is calculated from the length of output
# data.
# For the other digits, we use a combination of the length (either 5 or 6) and
# overlap of segments with others that have been identified according to this
# schema:
#    - 0, 6, and 9 have 6 segments
#        - 6 and 1 have one overlapping segment.
#        - 9 and 4 have four overlapping segments.
#        - 0 is the one remaining.
#   - 2, 3, and 5 have 5 segments
#        - 3 and 1 have two overlapping segments.
#        - 5 and 4 have three overlapping sgements.
#        - 2 is the one remaining.

def main():
    input_data = read_input_from_file(filename="input8b.txt", datatype=str,
        sep="\n")

    total = 0
    for line in input_data:
        (data_in, data_out) = line.split(" | ")
        #print(data_in, data_out)
        nums_in = list(map(str, data_in.split()))
        nums_in = [set(item) for item in nums_in]
        nums_out = list(map(str, data_out.split()))
        nums_out = [set(item) for item in nums_out]

        result = [0] * 10
        for num in nums_in:
            if len(num) == 2:
                result[1] = num
            elif len(num) == 3:
                result[7] = num
            elif len(num) == 4:
                result[4] = num
            elif len(num) == 7:
                result[8] = num
        # We must check inputs of length 5 and 6 *AFTER* we have checked
        # *ALL* of the inputs above, since we use them for basis of comparison.
        for num in nums_in:
            if len(num) == 5:     # 2, 3, or 5
                if len(result[1].intersection(num)) == 2:
                    result[3] = num
                elif len(result[4].intersection(num)) == 3:
                    result[5] = num
                else:
                    result[2] = num
            elif len(num) == 6:    # 0, 6, or 9
                if len(result[1].intersection(num)) == 1:
                    result[6] = num
                elif len(result[4].intersection(num)) == 4:
                    result[9] = num
                else:
                    result[0] = num

        # Build a dictionary that maps the segments to the corresponding
        # number to use for looking up numeric values.
        # Note: We must use string representation (instead of set) for
        # dictionary key so that key is hashable.
        d = {"".join(val): idx for idx, val in enumerate(result)}
        print(d)

        # Now compare all of the values in the output list to digit values
        # that we have identified based on the input to determine output
        # value for this row/line.
        out_list = list()
        for num in nums_out:
            for k, v in d.items():
                if set(k) == set(num):   # Convert to sets for comparison.
                    out_list.append(str(v))
                    break
        print(out_list, data_out, int("".join(out_list)))
        total += int("".join(out_list))

    print("Total of output values: {n}".format(n=total))

if __name__ == "__main__":
    main()