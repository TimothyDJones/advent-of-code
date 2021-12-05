# puzzle5b.py
from utils import *
from pprint import pprint, pformat

# Strategy:
# For each input line, determine if it represents a line (same x or y value).
# If so, then iterate through all points represented by that line. Check
# to see if each point exists in master dictionary of points. If so, then
# increment count for that point; if not, add the point to dictionary
# with count of 1. After all inputs checked, count number of points
# in dictionary with count greater than 1.
# Add check for diagonal lines, as well. Points are on diagonal if 
# the differences in the start and end x and y values are equal.

def main():
    input_data = read_input_from_file(filename="input5a.txt", datatype=str,
        sep="\n")
    points_dict = dict()
    for line in input_data:
        (start, end) = tuple(map(str, line.split(" -> ")))
        start = tuple(map(int, start.split(",")))
        end = tuple(map(int, end.split(",")))
        # print(start, end)
        if start[0] == end[0]:  # if x values are the same...
            for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                # If this point isn't already in dictionary, we return count of 0.
                # Either way, the point is added to dictionary, if doesn't exist,
                # or is updated.
                pt_count = points_dict.get((start[0], i), 0)
                points_dict[(start[0], i)] = (pt_count + 1)
        elif start[1] == end[1]:    # if y values are the same...
            for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                pt_count = points_dict.get((i, start[1]), 0)
                points_dict[(i, start[1])] = (pt_count + 1)
        # Check if points are on diagonal.
        elif (abs(start[0] - end[0]) == abs(start[1] - end[1])):
            print(start, end, (end[0] - start[0]), (end[1] - start[1]))
            dx = (end[0] - start[0]) // abs(start[0] - end[0])
            dy = (end[1] - start[1]) // abs(start[1] - end[1])
            for i in range(abs(start[0] - end[0]) + 1):
                pt_count = points_dict.get((start[0] + i * dx, 
                    start[1] + i * dy), 0)
            #    print("\t{p}".format(p=(start[0] + i, start[1] + i)))
                points_dict[(start[0] + i * dx, start[1] + i * dy)] = (pt_count + 1)

#    print("{d}".format(d=pformat(object=points_dict, indent=2)))

    # Get the list of points with count greater than 1 and find its length.
    num_overlap_pts = len([k for k, v in points_dict.items() if v > 1])

    print("Number of overlapping points: {n}".format(n=num_overlap_pts))

if __name__ == "__main__":
    main()