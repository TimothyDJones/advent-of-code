# puzzle10b.py
from utils import *
from pprint import pprint, pformat

# Strategy:
# In this puzzle, we use a stack-based approach to check for balanced sets
# of bracket pairs: (), [], {}, and <>.
# After removing all of the "corrupted" (unbalanced) lines, for each of the
# remaining "incomplete" lines, we take the opening characters remaining on
# the stack and find the associated closing characters in reverse order to
# make up the desired completion sequence and use them to calculate the
# score for each.

# Index 0 are the opening bracket and index 1 are the closing.
# Index 2 is the point score for each closing bracket type.
BRACKETS = [['(', ')', 1],
            ['[', ']', 2],
            ['{', '}', 3],
            ['<', '>', 4]]
POSITION_MULTIPLIER = 5     # Multiplier for each closing character added to complete string.

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
    # print(stack)
    if len(stack): return (False, "incomplete", "".join(stack))

    return (True, "balanced", "")

def main():
    input_data = read_input_from_file(filename="input10b.txt", datatype=str,
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
    completion_score_list = list()
    for line in input_data:
        (result, result_code, result_char) = balanced_brackets(line)
        print(line, result, result_code, result_char)
        # if not result and result_code == "corrupted":
        #     for i in range(len(BRACKETS)):
        #         if BRACKETS[i][1] == result_char:
        #             total_syntax_error_score += BRACKETS[i][2]
        #             break
        if not result and result_code == "incomplete":
            stack = list(result_char)[::-1]
            completion_score = 0
            for char_idx in range(len(stack)):
                for i in range(len(BRACKETS)):
                    if stack[char_idx] == BRACKETS[i][0]:
                        completion_score = ((completion_score * 5)
                            + BRACKETS[i][2])
                        break
            completion_score_list.append(completion_score)

    completion_score_list = sorted(completion_score_list)
    print(completion_score_list)

    print("Middle completion score: {n}".format(
        n=completion_score_list[(len(completion_score_list) // 2)]))

if __name__ == "__main__":
    main()