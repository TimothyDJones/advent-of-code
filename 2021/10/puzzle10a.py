# puzzle10a.py
from utils import *
from pprint import pprint, pformat

# Strategy:
# In this puzzle, we use a stack-based approach to check for balanced sets
# of bracket pairs: (), [], {}, and <>.

# Index 0 are the opening bracket and index 1 are the closing.
# Index 2 is the syntax error score
BRACKETS = [['(', ')', 3],
            ['[', ']', 57],
            ['{', '}', 1197],
            ['<', '>', 25137]]

def compare_brackets(opening, closing):
    for i in range(len(BRACKETS)):
        if BRACKETS[i][0] == opening and BRACKETS[i][1] == closing:
                return True

    return False

def balanced_brackets(test_str):
    stack = []  # Stack to store *opening* brackets.

    for char in test_str:
        # If char is one of the opening bracket types, we push it onto stack.
        if char in [b[0] for b in BRACKETS]:
            stack.append(char)
        # If char is one of the closing bracket types...
        if char in [b[1] for b in BRACKETS]:
            # If stack is empty, it means we have unbalanced situation, so
            # return False
            if not len(stack): return (False, "closed_before_opening", "")
            # Otherwise, "pop" the top (last) element and check to see if it
            # corresponds to the closing bracket character (char).
            # If not, we have a "corrupted" scenario, where the closing
            # bracket doesn't match the opening.
            if not compare_brackets(opening=stack.pop(), closing=char):
                return (False, "corrupted", char)

    # If after processing all characters in test_str, the stack is not empty,
    # then we have another unbalanced situation, so again return False.
    if len(stack): return (False, "incomplete", "".join(stack))

    return (True, "balanced", "")

def main():
    input_data = read_input_from_file(filename="input10a.txt", datatype=str,
        sep="\n")

    # input_data = """
    # [({(<(())[]>[[{[]{<()<>>
    # [(()[<>])]({[<{<<[]>>(
    # {([(<{}[<>[]}>{[]{[(<()>
    # (((({<>}<{<{<>}{[]{[]{}
    # [[<[([]))<([[{}[[()]]]
    # [{[{({}]{}}([{[{{{}}([]
    # {<[[]]>}<{[{[{[]{()[[[]
    # [<(<(<(<{}))><([]([]()
    # <{([([[(<>()){}]>(<<{{
    # <{([{{}}[<[[[<>{}]]]>[]]
    # """
    # input_data = list(map(str, input_data.strip().split("\n")))

    total_syntax_error_score = 0
    for line in input_data:
        (result, result_code, result_char) = balanced_brackets(line)
        print(line, result, result_code, result_char)
        if not result and result_code == "corrupted":
            for i in range(len(BRACKETS)):
                if BRACKETS[i][1] == result_char:
                    total_syntax_error_score += BRACKETS[i][2]
                    break

    print("Total syntax error score: {n}".format(n=total_syntax_error_score))

if __name__ == "__main__":
    main()