# puzzle8a.py

def main():
    accum = 0
    index = 0

    instrs = read_file()

    while True:
        instr = instrs[index]
        # If instruction already executed, exit loop.
        if instr["executed"]:
            break
        else:
            # Set flag that this instruction has been executed.
            instrs[index]["executed"] = True

        if instr["oper"] == "nop":
            index += 1
        elif instr["oper"] == "jmp":
            index += instr["incr"]
        elif instr["oper"] == "acc":
            accum += instr["incr"]
            index += 1
        else:
            raise ValueError("Invalid instruction: " + str(instr["oper"]))


    print("Accumulator value: " + str(accum))

def read_file():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

        items = []
        index = 0
        for line in lines:
            elems = line.split(" ")
            items.append({"idx": index, "oper": elems[0], "incr": int(elems[1]), "executed": False})
    
        return items

if __name__ == "__main__":
    main()