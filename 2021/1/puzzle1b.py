# puzzle1b.py
def main():
    input_file = open("input1b.txt", "r")
    lines = input_file.readlines()

    num_measurements = len(lines)

    # Use three consecutive measurements as sliding window and sum them.
    sliding_window = list()
    for i in range(num_measurements - 2):
        sliding_window.append(int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2]))

    num_increasing = 0

    for i in range(1, num_measurements - 2):
        if int(sliding_window[i]) > int(sliding_window[i - 1]):
            print("{a}, {b} +".format(a=int(sliding_window[i - 1]), b=int(sliding_window[i])))
            num_increasing += 1
        else:
            print("{a}, {b} -".format(a=int(sliding_window[i - 1]), b=int(sliding_window[i])))

    print("Number of increasing measurements: {n}\n".format(n=num_increasing))

if __name__ == "__main__":
    main()