# puzzle04b.py
import string
from pprint import pformat
import re

def main():
    input_file = open("input04.txt", "r")
    # input_file = open("test.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    card_scores = dict()
    total_scratchcards = 0
    
    # card_scores = {card_num: [card_score, card_count]}
    # Initialize card_scores dictionary
    for i in range(1, num_lines + 1):
        card_scores[i] = [0, 1]
        
    # print("{s}".format(s=pformat(object=card_scores, indent=2)))

    for line in lines:
        card, data = line.split(": ")
        _, card_num = card.split()
        card_num = int(card_num)
        winning_numbers, possible_numbers = data.split(" | ")
        winning_numbers = winning_numbers.split()
        possible_numbers = possible_numbers.split()
        win_count = 0
        for num in winning_numbers:
            if num in possible_numbers:
                win_count += 1
        if win_count:
            card_scores[card_num][0] = 2**(win_count - 1)
            for n in range(card_num + 1, card_num + win_count + 1):
                if n <= num_lines:
                    card_scores[n][1] += card_scores[card_num][1]
                
    print("{s}".format(s=pformat(object=card_scores, indent=2)))
    
    for i in range(1, num_lines + 1):
        total_scratchcards += card_scores[i][1]
    
    # print("{p}".format(p=pformat(object=valid_part_nums, indent=2)))
        
    print("Total scratchcards: {n}\n".format(n=total_scratchcards))
    # Answer: 6874754

if __name__ == "__main__":
    main()