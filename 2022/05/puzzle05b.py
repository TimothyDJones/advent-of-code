# puzzle05b.py
import string

def main():
    input_file = open("input05.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    overlap_pairs_count = 0
    stack = [
        [],
        ["M", "J", "C", "B", "F", "R", "L", "H"],
        ["Z", "C", "D"],
        ["H", "J", "F", "C", "N", "G", "W"],
        ["P", "J", "D", "M", "T", "S", "B"],
        ["N", "C", "D", "R", "J"],
        ["W", "L", "D", "Q", "P", "J", "G", "Z"],
        ["P", "Z", "T", "F", "R", "H"],
        ["L", "V", "M", "G"],
        ["C", "B", "G", "P", "F", "Q", "R", "J"]
    ]
    top_crates = ""

    for i in range(0, num_lines):
        line = lines[i].strip()
        if "move" in line:
            item = line.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(",")
            # print(item[0], item[1], item[2], stack[int(item[1])][:int(item[0])])
            # print(stack[int(item[1])], stack[int(item[2])], stack[int(item[1])][-int(item[0]):])
            stack[int(item[2])].extend(stack[int(item[1])][-int(item[0]):])
            del stack[int(item[1])][(len(stack[int(item[1])]) - int(item[0])):]
            # print(stack[int(item[1])], stack[int(item[2])])

    for i in range (1, len(stack)):
        top_crates += stack[i][-1]

    print("Crates on top of each stack: {n}\n".format(n=top_crates))
    # Answer: RMHFJNVFP

if __name__ == "__main__":
    main()
