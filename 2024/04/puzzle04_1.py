

def main():
    data = list()
    dirs = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0,),
        (1, 1)
    ]
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
    
    for t_x in x_set:
        X, Y = t_x
        for DX, DY in dirs:
            t_m = (X + DX, Y + DY)
            t_a = (X + 2*DX, Y + 2*DY)
            t_s = (X + 3*DX, Y + 3*DY)
            if t_m in m_set and t_a in a_set and t_s in s_set:
                num_xmas += 1
    
    print("Number of 'XMAS': {s}".format(s=num_xmas))
    
    
if __name__ == "__main__":
    main()