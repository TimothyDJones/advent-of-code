# puzzle02b.py
def main():
    # A = Rock --> 1 point
    # B = Paper --> 2 points
    # C = Scissors --> 3 points
    # X = Lose --> 0 points
    # Y = Draw --> 3 points
    # Z = Win --> 6 points

    pairs = {
        ("A", "X"): (0, 3), ("A", "Y"): (3, 1), ("A", "Z"): (6, 2),
        ("B", "X"): (0, 1), ("B", "Y"): (3, 2), ("B", "Z"): (6, 3),
        ("C", "X"): (0, 2), ("C", "Y"): (3, 3), ("C", "Z"): (6, 1)
        }

    input_file = open("input02b.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    total_score = 0

    for i in range(0, num_lines):
        round = tuple(lines[i].strip().split(" "))
        result = pairs[round]
        total_score += (result[0] + result[1])
        # print(round, result, total_score)

    print("Total score: {n}\n".format(n=total_score))
    # Answer: 10398

if __name__ == "__main__":
    main()