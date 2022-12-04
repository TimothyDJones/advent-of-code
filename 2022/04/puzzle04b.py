# puzzle04b.py
import string

def main():
    input_file = open("input04.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    overlap_pairs_count = 0

    for i in range(0, num_lines):
        line = lines[i].strip()
        (elf1, elf2) = (line.split(",")[0].split("-"), line.split(",")[1].split("-"))
        (set1, set2) = (set(list(range(int(elf1[0]), int(elf1[1]) + 1))),
            set(list(range(int(elf2[0]), int(elf2[1]) + 1))))
        if set1.intersection(set2):
            overlap_pairs_count += 1

    print("Total pairs with overlapping range: {n}\n".format(n=overlap_pairs_count))
    # Answer: 798

if __name__ == "__main__":
    main()
