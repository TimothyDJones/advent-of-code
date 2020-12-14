# puzzle3a.py
def main():
    horiz_step = 3
    vert_step = 1
    tree_char = "#"

    horiz_pos = 0
    trees = 0

    input_file = open("input.txt", "r")
    lines = input_file.readlines()
    
    line_len = len(lines[0]) - 1    # Subtract 1 to account for '\n'
    lines = lines[1:]
    for line in lines:
        horiz_pos = (horiz_pos + horiz_step) % line_len
        if line[horiz_pos] == tree_char:
            trees += 1

    print("Trees encountered: " + str(trees))         

if __name__ == "__main__":
    main()