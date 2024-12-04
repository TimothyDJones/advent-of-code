

def main():
    data = list()
    num_xmas = 0

    with open("input04.txt", "r") as f:
        line = f.readline()
        while line:
            data.append(line.strip())
            line = f.readline()
            
    # print(data)
    
    # Sets of coordinates for each of "X", "M", "A", and "S".
    x_set, m_set, a_set, s_set = set(), set(), set(), set()
    
    for y, f in enumerate(data):
        for x, c in enumerate(f):
            coord = (x, y)
            if c == "X": x_set.add(coord)
            elif c == "M": m_set.add(coord)
            elif c == "A": a_set.add(coord)
            elif c == "S": s_set.add(coord)
    
    # print(x_set, m_set, a_set, s_set)
    
    for t_a in a_set:
        # print(t_a)
        X, Y = t_a
        # Check diagonally from each "center" "A" for "M" and "S" on "corners"...
        up_left, up_right, bottom_left, bottom_right = (X-1, Y-1), (X+1, Y-1), (X-1, Y+1), (X+1, Y+1)
        # print(up_left, up_right, bottom_left, bottom_right)
        if up_left in m_set and up_right in m_set and bottom_left in s_set and bottom_right in s_set:
            # print("X-MAS")
            num_xmas += 1
            continue
        # Rotate through other 3 combinations of positions...
        for i in range(3):
            up_left, up_right, bottom_right, bottom_left = up_right, bottom_right, bottom_left, up_left
            # print(up_left, up_right, bottom_left, bottom_right)
            if up_left in m_set and up_right in m_set and bottom_left in s_set and bottom_right in s_set:
                # print("X-MAS")
                num_xmas += 1
                break
    
    print("Number of 'X-MAS': {s}".format(s=num_xmas))
    
    
if __name__ == "__main__":
    main()