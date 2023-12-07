# puzzle06a.py
from collections import Counter
from random import randint
import string
from pprint import pformat
import re

CARD_MAP = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

HAND_TYPE_MAP = {
    "High Card": 1,
    "One Pair": 2,
    "Two Pair": 3,
    "Three of a Kind": 4,
    "Full House": 5,
    "Four of a Kind": 6,
    "Five of a Kind": 7
}

def parse_data():
    input_file = open("input07.txt", "r")
    # input_file = open("test.txt", "r")
    lines = input_file.readlines()
    
    data_map = list()
    
    for line in lines:
        hand, bid = line.split()
        data_map.append([hand, int(bid)])

    # print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map)

def get_hand_type(hand):
    """
    Determine the type of hand using HAND_TYPE_MAP of
    the `hand`.
    """
    # return randint(1, 7)
    hand_count = Counter(hand).most_common()
    if len(hand_count) == 5:
        return HAND_TYPE_MAP["High Card"]
    elif len(hand_count) == 4:
        return HAND_TYPE_MAP["One Pair"]
    elif len(hand_count) == 1:
        return HAND_TYPE_MAP["Five of a Kind"]
    elif len(hand_count) == 3:
        pairs = len([k for k, v in hand_count if v == 2])
        if pairs == 2:
            return HAND_TYPE_MAP["Two Pair"]
        else:
            return HAND_TYPE_MAP["Three of a Kind"]
    elif len(hand_count) == 2:
        four_of_kind = len([k for k, v in hand_count if v == 4])
        if four_of_kind:
            return HAND_TYPE_MAP["Four of a Kind"]
        else:
            return HAND_TYPE_MAP["Full House"]    

def main():
    data = parse_data()
    
    new_data = list()
    # new_data format: ["hand", "bid", "ranking_score", "hand_type"]
    total_winnings = 0
    
    for game in data:
        ranking_score = 0
        for i in range(len(game[0])):
            # Ranking score is used to determine *relative* ordering
            # of this hand among hands of *SAME TYPE*.
            # Need to use "100" as base for exponent, because "10" is too
            # small to get ordering correct!
            ranking_score += CARD_MAP[game[0][i]] * (100 ** (5 - i))
        game.append(ranking_score)
        game.append(get_hand_type(game[0]))
        new_data.append(game)
        
    # Sort the list using both `hand_type` and `ranking_score` as keys.
    new_data.sort(key=lambda x: [(7 - x[3]), (-1) * x[2]], reverse=True)
    # print("{d}".format(d=pformat(object=new_data, indent=2)))
    
    total_winnings = sum([rank * game[1] for rank, game in enumerate(new_data, start=1)])

    print("Total winnings: {n}\n".format(n=total_winnings))
    # Answer: 246424613

if __name__ == "__main__":
    main()