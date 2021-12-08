# puzzle8a.py
from utils import *
from pprint import pprint, pformat

# Strategy:
# Since 1, 4, 7, and 8 each have a unique number of segments (2, 4, 3, and 7,
# respectively), we can find the count of these directly from the output.
# We use a list to store the relevant information. The index of the list is
# the number of segments used, which is calculated from the length of output
# data.

def main():
    input_data = read_input_from_file(filename="input8a.txt", datatype=str,
        sep="\n")

    seg_count = [0] * 9
    for line in input_data:
        (data_in, data_out) = line.split(" | ")
        #print(data_in, data_out)
        nums_out = list(map(str, data_out.split()))
        len_nums_out = [len(item) for item in nums_out]
        for num_segs in len_nums_out:
            seg_count[num_segs] += 1

    count_1_4_7_8 = seg_count[2] + seg_count[4] + seg_count[3] + seg_count[7]
    print("Count of digits 1, 4, 7, and 8: {n}".format(n=count_1_4_7_8))

if __name__ == "__main__":
    main()