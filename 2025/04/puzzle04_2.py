import copy

def main():

    with open("input04.txt", "r") as f:
        data = [list(line.strip()) for line in f.readlines()]
        
    # Add placeholder empty positions at top and bottom and each end.
    data.insert(0, list("." * len(data[0])))    # top
    data.append(list("." * len(data[0])))       # bottom
    new_data = list()
    for row in data:
        row.insert(0, ".")
        row.append(".")
        new_data.append(row)
    data = new_data
    # print(data)
        
    # Check each *ORIGINAL* position for number of adjacent paper rolls.
    total_rolls = list()
    while True:
        # print(total_rolls)
        # print(data)
        accessible_rolls = list()
        new_data = copy.deepcopy(data)
        for row in range(1, len(data) - 1):
            for col in range(1, len(data[0]) - 1):
                if data[row][col] == ".":
                    continue
                if data[row][col] == "@":
                    num_adj = 0
                    for r in range(-1, 2):
                        if num_adj >= 4:
                            break
                        for c in range(-1, 2):
                            if num_adj >= 4:
                                break
                            if r == 0 and c == 0:   # this is "self"
                                continue
                            if data[row+r][col+c] == "@":
                                num_adj += 1
                                
                    if num_adj >= 4:
                        continue
                        
                    accessible_rolls.append([row, col])
                    # print(accessible_rolls)
                    # Replace this roll (now removed) with "blank".
                    new_data[row][col] = "."
                    
        if accessible_rolls:
            total_rolls.extend(accessible_rolls)
            data = new_data
        else:
            break
                            
    print("Number of accessible rolls: {r}".format(r=len(total_rolls)))

if __name__ == "__main__":
    main()
