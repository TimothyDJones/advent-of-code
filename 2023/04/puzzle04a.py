# puzzle04a.py
import string
from pprint import pformat
import re

def main():
    input_file = open("input04.txt", "r")
    # input_file = open("test.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    card_scores = list()

    for line in lines:
        card, data = line.split(": ")
        _, card_num = card.split()
        winning_numbers, possible_numbers = data.split(" | ")
        winning_numbers = winning_numbers.split()
        possible_numbers = possible_numbers.split()
        win_count = 0
        for num in winning_numbers:
            if num in possible_numbers:
                win_count += 1
        if win_count:
            card_scores.append(2**(win_count - 1))
        else:
            card_scores.append(0)
                
    print("{s}".format(s=pformat(object=card_scores, indent=2)))
    
    # print("{p}".format(p=pformat(object=valid_part_nums, indent=2)))
        
    print("Total of card scores: {n}\n".format(n=sum(card_scores)))
    # Answer: 21088

if __name__ == "__main__":
    main()