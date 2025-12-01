

def main():
    DIR_MAP = {
        "R": 1,
        "L": -1
    }
    count_zero = 0

    with open("input01.txt", "r") as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    pos = 50

    for line in lines:
        _dir = line[0]
        move = DIR_MAP[_dir] * int(line[1:])
        tmp_pos = pos + move
        # print(tmp_pos)
        while True:
            if tmp_pos >= 100:
                pos = tmp_pos - 100
            elif tmp_pos < 0:
                pos = tmp_pos + 100
            else:
                pos = tmp_pos
                
            if pos >= 100 or pos < 0:
                tmp_pos = pos
            else:
                break
        # print("\t", pos)

        if not pos:
            count_zero += 1

    print("Number of times stopped on 0: {cz}".format(cz=count_zero))


if __name__ == "__main__":
    main()
