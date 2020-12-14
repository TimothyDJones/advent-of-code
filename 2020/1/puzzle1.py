# puzzle1.py
def main():
    target_value = 2020

    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    for i in lines:
        for j in lines:
            for k in lines:
                if int(i) + int(j) + int(k) == target_value:
                    print(int(i), int(j), int(k), int(i) * int(j) * int(k))
                    break

if __name__ == "__main__":
    main()