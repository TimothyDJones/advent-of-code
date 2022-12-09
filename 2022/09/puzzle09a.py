# puzzle09a.py
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
    head = [0, 0]
    tail = [0, 0]
    positions_visited = []
    directions = {
        "L": [-1, 0],
        "R": [1, 0],
        "U": [0, 1],
        "D": [0, -1]
    }
    sign = lambda n: (n>0) - (n<0)

    positions_visited.append(tail.copy())

    for i in range(0, num_lines):
        (direction, count) = lines[i].strip().split(" ")
        # print(direction, count)
        for j in range(int(count)):
            head[0] += directions[direction][0]
            head[1] += directions[direction][1]
            # Check to see if `tail` is adjacent to `head`.
            tail_adj = False
            for k in range(len(adjacent)):
                temp_head = head.copy()
                temp_head[0] += adjacent[k][0]
                temp_head[1] += adjacent[k][1]
                # print("\t\t", tail, temp_head)
                if temp_head == tail:
                    tail_adj = True
                    break
            # If `tail` is *NOT* adjacent to `head`, move the tail.
            if not tail_adj:
                tail[0] += sign(head[0] - tail[0])
                tail[1] += sign(head[1] - tail[1])
                positions_visited.append(tail.copy())
            # print("\t", head, tail, tail_adj, "\n", positions_visited)
        # print(head, tail)

    unique_posns = len({tuple(posn) for posn in positions_visited})
    print("Number of unique positions visited by tail: {n}\n".format(n=unique_posns))
    # Answer: 6011

if __name__ == "__main__":
    main()
