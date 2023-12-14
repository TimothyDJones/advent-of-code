# puzzle13b.py
from pprint import pformat

def parse_data():
    # input_file = open("input13.txt", "r")
    input_file = open("test.txt", "r")
    data = input_file.read()
    data_map = [section.split("\n") for section in data.split("\n\n")]

    # print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map[0:1]) 

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

def replace_char(grid, row, col, char):
    row_chars = list(grid[row])
    row_chars[col] = char
    grid[row] = "".join(row_chars)
    print("{d}".format(d=pformat(object=grid, indent=2)))
    return(grid)

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
        
        orig_scores = (horizontal_score if horizontal_score else 0, 
            vertical_score if vertical_score else 0)
        print("original scores: ", orig_scores)
        for row in range(len(section)):
            for col in range(len(section[0])):
                if section[row][col] == "#":
                    new_section = replace_char(section, row, col, ".")
                    horizontal_score = check_reflection(new_section)
                    vertical_score = check_reflection(transpose_pattern(new_section))
                    print(row, col, ": ", horizontal_score, horizontal_score != orig_scores[0], vertical_score, vertical_score != orig_scores[1])
                    if (horizontal_score and horizontal_score != orig_scores[0] ):
                        break
                    elif (vertical_score and vertical_score != orig_scores[1]):
                        break
                elif section[row][col] == ".":
                    new_section = replace_char(section, row, col, "#")
                    horizontal_score = check_reflection(new_section)
                    vertical_score = check_reflection(transpose_pattern(new_section))
                    if (horizontal_score and horizontal_score != orig_scores[0]):
                        break
                    elif (vertical_score and vertical_score != orig_scores[1]):
                        break
        
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