# puzzle02a.py
def main():
    # A, X = Rock --> 1 point
    # B, Y = Paper --> 2 points
    # C, Z = Scissors --> 3 points
    # Score for each round: Choice *plus*:
    #   0 for loss
    #   3 for draw/tie
    #   6 for win

    pairs = {
        ("A", "X"): (3, 1), ("A", "Y"): (6, 2), ("A", "Z"): (0, 3),
        ("B", "X"): (0, 1), ("B", "Y"): (3, 2), ("B", "Z"): (6, 3),
        ("C", "X"): (6, 1), ("C", "Y"): (0, 2), ("C", "Z"): (3, 3)
        }

    input_file = open("input02a.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    total_score = 0

    for i in range(0, num_lines):
        round = tuple(lines[i].strip().split(" "))
        result = pairs[round]
        total_score += (result[0] + result[1])
        # print(round, result, total_score)

    print("Total score: {n}\n".format(n=total_score))
    # Answer: 13009

if __name__ == "__main__":
    main()