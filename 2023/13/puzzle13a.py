# puzzle13a.py
from pprint import pformat

def parse_data():
    input_file = open("input13.txt", "r")
    # input_file = open("test.txt", "r")
    data = input_file.read()
    data_map = [section.split("\n") for section in data.split("\n\n")]

    # print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map) 

def check_reflection(pattern):
    split = 0
    mismatch = False
    # print("Check for split...")
    for i in range(1, len(pattern)):
        # print(i, pattern[i - 1], pattern[i], pattern[i - 1] == pattern[i])
        if pattern[i - 1] == pattern[i]:
            split = i
            # print(pattern[i - 1], pattern[i], i)

            # Check that pattern matches all the way until edge of grid.
            mismatch = False
            for j in range(0, min(len(pattern) - split, split)):
                # print(split, split - j - 1, pattern[split - j - 1], pattern[split + j], split + j)
                if not pattern[split - j - 1] == pattern[split + j]:
                    mismatch = True
                    break
            if not mismatch:
                return split

    # print("check_reflection", split, mismatch)      
    return None
    
def transpose_pattern(pattern):
    _tmp = [list(row) for row in pattern]
    transpose = list(zip(*_tmp))
    # print("{d}".format(d=pformat(object=transpose, indent=2)))
    # new_pattern = ["".join(item) for item in row for row in transpose]
    new_pattern = list()
    for row in transpose:
        new_pattern.append("".join(x for x in row))
    
    
    # print("{d}".format(d=pformat(object=new_pattern, indent=2)))
    
    return(new_pattern)

def main():
    reflection_scores = list()
    data = parse_data()
    
    
    for idx, section in enumerate(data):
        print("Section {n}".format(n=idx))
        # Check for *horizontal* reflection.
        print("{d}".format(d=pformat(object=section, indent=2)))
        horizontal_score = check_reflection(section)
        # Check for *vertical* reflection.
        transpose_section = transpose_pattern(section)
        print("{d}".format(d=pformat(object=transpose_section, indent=2)))
        vertical_score = check_reflection(transpose_section)        
        
        if horizontal_score:
            print("horizontal score: {s}".format(s=horizontal_score * 100))
            reflection_scores.append(horizontal_score * 100)
        elif vertical_score:
            print("vertical score: {s}".format(s=vertical_score))
            reflection_scores.append(vertical_score)
    
    print("scores: {s}".format(s=pformat(object=reflection_scores, indent=2)))
    print("Sum of reflection scores: {n}\n".format(n=sum(reflection_scores)))
    # Answer: 34100

if __name__ == "__main__":
    main()