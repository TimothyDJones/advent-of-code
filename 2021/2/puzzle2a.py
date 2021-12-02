# puzzle2a.py
def main():
    input_file = open("input2a.txt", "r")
    lines = input_file.readlines()

    num_cmds = len(lines)
    h_pos = 0   # horizontal position
    depth = 0

    for i in range(num_cmds):
        (cmd, amt) = (lines[i].split()[0], int(lines[i].split()[1]))
        if cmd in ["forward"]:
            h_pos += amt
        elif cmd in ["up"]:
            depth -= amt
        elif cmd in ["down"]:
            depth += amt

    print("Horizontal position: {h}\nDepth: {d}\nProduct: {p}\n"
        .format(h=h_pos, d=depth, p=(h_pos * depth)))

if __name__ == "__main__":
    main()