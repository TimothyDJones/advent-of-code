# puzzle02b.py
from pprint import pformat
import string

MAX_BLOCKS_MAP = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def main():
    input_file = open("input02.txt", "r")
    # input_file = open("test.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    round_power = list()

    for line in lines:
        b_winning_game = True
        game, game_data = line.split(": ")
        _, game_num = game.split()
        game_num = int(game_num)
        min_round_data = {
            "red": 0,
            "green": 0,
            "blue": 0
        }        
        for _round in game_data.split("; "):
            round_data = _round.split(", ")
            for item in round_data:
                num_blocks, block_color = item.split()
                if int(num_blocks) > min_round_data[block_color]:
                    min_round_data[block_color] = int(num_blocks)
                    
            # print("{rd}".format(rd=pformat(object=min_round_data, indent=2)))
        
        round_power.append(min_round_data["red"] * min_round_data["green"]
            * min_round_data["blue"])
    
    # print("{r}".format(r=pformat(object=round_power, indent=2)))
    print("Total of round powers: {n}\n".format(n=sum(round_power)))
    # Answer: 72227

if __name__ == "__main__":
    main()