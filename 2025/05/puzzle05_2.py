

def main():
    ingr_range_list = list()
    merged_ingr_ranges = list()
    num_valid_ingr = 0

    with open("input05.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    for item in data:
        if "-" in item:
            ingr_range_list.append(list(map(int, (item.split("-")))))
        elif "\n" in item:
            break
            
    # print(ingr_range_list)
            
    merged_ingr_ranges = merge_intervals(intervals=ingr_range_list)
    # print(merged_ingr_ranges)
    num_valid_ingr = sum([((r[1] - r[0]) + 1) for r in merged_ingr_ranges])        

    print("Number of valid ingredient IDs: {i}".format(i=num_valid_ingr))

def merge_intervals(intervals: list):
    if not intervals:
        return []
    
    # Sort the intervals by the start value
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        # Check if there is an overlap
        if current[0] <= last_merged[1]: 
            # Merge the intervals
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
    
    return merged

if __name__ == "__main__":
    main()
