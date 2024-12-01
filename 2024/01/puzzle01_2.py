

def main():
    left, right = list(), list()

    with open("input01.txt", "r") as f:
        line = f.readline()
        while line:
            vals = line.split(sep=" ", maxsplit=1)
            left.append(int(vals[0]))
            right.append(int(vals[1]))
            line = f.readline()

    left = sorted(left)
    right = sorted(right)
    
    print(left[:5])

    similarity = list()

    for i in range(len(left)):
        similarity.append(left[i] * right.count(left[i]))

    print("Sum of similarity scores: {sd}".format(sd=sum(similarity)))
    
    
if __name__ == "__main__":
    main()