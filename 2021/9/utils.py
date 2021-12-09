
def read_input_from_file(filename, datatype, sep="\n"):
    with open(filename, "r") as f:
        data = f.read().strip().split(sep)
        return list(map(datatype, data))

def nums(line):
    return list(map(int, line))