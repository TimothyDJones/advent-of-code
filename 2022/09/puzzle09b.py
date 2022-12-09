# puzzle09b.py
import string

def main():
    input_file = open("input09.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)

    adjacent = [
        [-1, 1], [0, 1], [1, 1],
        [-1, 0], [0, 0], [1, 0],
        [-1, -1], [0, -1], [1, -1]
        ]
    KNOTS = 10
    rope = [[0, 0] for i in range(KNOTS)]  # `head` --> rope[0], `tail` --> rope[9]
    positions_visited = []
    directions = {
        "L": [-1, 0],
        "R": [1, 0],
        "U": [0, 1],
        "D": [0, -1]
    }
    sign = lambda n: (n>0) - (n<0)

    positions_visited.append(rope[(KNOTS-1)].copy())

    for i in range(0, num_lines):
        (direction, count) = lines[i].strip().split(" ")
        # print(direction, count)
        for j in range(int(count)):
            # Move `head` (a.k.a., rope[0]).
            rope[0][0] += directions[direction][0]
            rope[0][1] += directions[direction][1]
            # Check to see if each `knot` is adjacent to its predecessor.
            for knot in range(1, KNOTS):
                knot_adj = False
                for k in range(len(adjacent)):
                    temp_pred = rope[knot-1].copy()
                    temp_pred[0] += adjacent[k][0]
                    temp_pred[1] += adjacent[k][1]
                    # print("\t\t", tail, temp_head)
                    if temp_pred == rope[knot]:
                        knot_adj = True
                        break
                # If `knot` is *NOT* adjacent to predecessor, move the knot.
                if not knot_adj:
                    rope[knot][0] += sign(rope[knot-1][0] - rope[knot][0])
                    rope[knot][1] += sign(rope[knot-1][1] - rope[knot][1])
                    if knot == (KNOTS - 1):
                        positions_visited.append(rope[knot].copy())
                # print("\t", head, tail, tail_adj, "\n", positions_visited)
            # print(head, tail)

    unique_posns = len({tuple(posn) for posn in positions_visited})
    print("Number of unique positions visited by tail: {n}\n".format(n=unique_posns))
    # Answer: 6011

if __name__ == "__main__":
    main()
