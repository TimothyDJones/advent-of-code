

def main():
    data = list()
    safe = 0

    with open("input02.txt", "r") as f:
        line = f.readline()
        while line:
            vals = line.split(sep=" ")
            vals = [int(i) for i in vals]
            if all(i < j and (j - i) <= 3 for i, j in zip(vals, vals[1:])):
                safe += 1
            elif all(i > j and (i - j) <= 3 for i, j in zip(vals, vals[1:])):
                safe += 1
            line = f.readline()

    print("Number of safe reports: {s}".format(s=safe))
    
    
if __name__ == "__main__":
    main()