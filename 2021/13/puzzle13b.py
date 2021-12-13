# puzzle13b.py
from utils import *
from pprint import pprint, pformat

# Strategy:
# For each fold, all point on the fold line are removed (i.e., points with the
# specified x or y value). Subsequently, remaining points are adjusted by
# having their corresponding coordinate (x or y) reduced by the same amount
# as their distance from the fold line if they are to the right (x greater than)
# or below (y greater than) the fold line. If the new points overlap with
# existing, then only one is retained.

def main():
    (points, *folds) = read_input_from_file(filename="input13b.txt",
        datatype=str, sep="\n\n")
    points = points.splitlines()
    points = [tuple(map(int, point.split(","))) for point in points]
    # print(points)

    folds = [fold.splitlines() for fold in folds][0]
    folds = [tuple(map(str, fold.replace("fold along ", "").split("=")))
        for fold in folds]
    # print(folds)

    for fold in folds:
        remove_index = list()
        if fold[0] == "x":  # Fold left
            x = int(fold[1])
            for i in range(len(points)):
                if points[i][0] == x:
                    remove_index.append(i)
                elif points[i][0] > x:
                    points[i] = (x - abs(x - points[i][0]), points[i][1])
                # print(points[i])
        if fold[0] == "y":  # Fold up
            y = int(fold[1])
            for i in range(len(points)):
                if points[i][1] == y:
                    remove_index.append(i)
                elif points[i][1] > y:
                    points[i] = (points[i][0], y - abs(y - points[i][1]))

        for i in remove_index:
            del points[i]

        #print(points, list(set(points)))
        points = list(set(points))
        #print(points)

        print("Total points visible after fold {f}: {n}".format(
            f=fold, n=len(points)))

    # print(points)
    # For part 2, create a 2D array of remaining visible points, which
    # represent 8 capital letters for the code to unlock camera.
    code_list = list()
    for i in range(7):
        row = list()
        for j in range(40):
            if (j, i) in points:
                row.append("X")
            else:
                row.append(" ")
        code_list.append("".join(row))
    pprint(code_list)

if __name__ == "__main__":
    main()