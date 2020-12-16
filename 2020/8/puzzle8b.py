# puzzle8a.py

def main():
    instrs = read_file()
    for i in range(len(instrs)):
        instrs = read_file()
        # Swap the "jmp" and "nop" operations for
        # each of the possibilities until we find
        # a case where an instruction is not re-executed.
        if instrs[i]["oper"] in ["jmp", "nop"]:
            instrs[i] = swap_oper(instrs[i])
        else:
            # Can skip these cases, since they will have
            # no difference.
            continue
        
        soln_found = True

        accum = 0
        index = 0

        while True:
            try:
                instr = instrs[index]
                # If instruction already executed, exit loop.
                if instr["executed"]:
                    soln_found = False
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
            except Exception:
                break
            
        if soln_found:
            break

    print("Accumulator value: " + str(accum))

def swap_oper(instr):
    if instr["oper"] == "jmp":
        instr["oper"] = "nop"
    else:
        instr["oper"] = "jmp"
    
    return instr

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