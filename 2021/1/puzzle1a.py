# puzzle1a.py
def main():
    input_file = open("input1a.txt", "r")
    lines = input_file.readlines()

    num_measurements = len(lines)
    num_increasing = 0

    for i in range(1, num_measurements):
        if int(lines[i]) > int(lines[i - 1]):
            print("{a}, {b} +".format(a=int(lines[i - 1]), b=int(lines[i])))
            num_increasing += 1
        else:
            print("{a}, {b} -".format(a=int(lines[i - 1]), b=int(lines[i])))

    print("Number of increasing measurements: {n}\n".format(n=num_increasing))

if __name__ == "__main__":
    main()