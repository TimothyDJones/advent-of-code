# puzzle5a.py

# For rows:
#   "B" (back) is binary 1
#   "F" (front) is binary 0
# For columns:
#   "L" (left) is binary 0
#   "R" (right) is binary 1

def main():
    boarding_passes = read_file()
    
    max_seat_nbr = 0

    for bp in boarding_passes:
        bp = bp.rstrip("\n")
        col = int(bp[:7].replace("B", "1").replace("F", "0"), 2)
        row = int(bp[-3:].replace("L", "0").replace("R", "1"), 2)
        seat_nbr = col * 8 + row

        if seat_nbr > max_seat_nbr:
            max_seat_nbr = seat_nbr

    print("Highest seat ID: " + str(max_seat_nbr))

            
def read_file():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    return lines

if __name__ == "__main__":
    main()