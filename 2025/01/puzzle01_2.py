

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
        last_pos = pos
        _dir = line[0]
        move = DIR_MAP[_dir] * int(line[1:])
        pos = (pos + move) % 100
        count_zero += ((abs(move) // 100)
			+ (1 if (((pos >= last_pos and move <= 0)
					or (pos <= last_pos and move >= 0))
					and (last_pos != 0)
					or pos == 0)
				else 0))
        # print(line, last_pos, pos, count_zero)

    print("Number of times crosses *OR* stops on 0: {cz}".format(cz=count_zero))


if __name__ == "__main__":
    main()
