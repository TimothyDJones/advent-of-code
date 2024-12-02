

def main():
    data = list()
    safe = 0

    with open("input02.txt", "r") as f:
        line = f.readline()
        while line:
            vals = line.split(sep=" ")
            vals = [int(i) for i in vals]
            if is_safe(vals):
                safe += 1
            else:
                for i in range(len(vals)):
                    if is_safe(vals[:i] + vals[i + 1:]):
                        safe += 1
                        break
            line = f.readline()

    print("Number of safe reports: {s}".format(s=safe))

def is_safe(vals: list):
    if all(i < j and (j - i) <= 3 for i, j in zip(vals, vals[1:])):
        return True
    elif all(i > j and (i - j) <= 3 for i, j in zip(vals, vals[1:])):
        return True
        
    return False
    
if __name__ == "__main__":
    main()