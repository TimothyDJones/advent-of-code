# puzzle02a.py
import string

MAX_BLOCKS_MAP = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def main():
    input_file = open("input02.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)
    winning_games = list()

    for line in lines:
        b_winning_game = True
        game, game_data = line.split(": ")
        _, game_num = game.split()
        game_num = int(game_num)
        for _round in game_data.split("; "):
            round_data = _round.split(", ")
            for item in round_data:
                num_blocks, block_color = item.split()
                if int(num_blocks) > MAX_BLOCKS_MAP[block_color]:
                    b_winning_game = False
                    break        
        
        if b_winning_game:
            winning_games.append(game_num)
        
    print("Total of winning game IDs: {n}\n".format(n=sum(winning_games)))
    # Answer: 2716

if __name__ == "__main__":
    main()