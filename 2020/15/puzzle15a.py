# puzzle15a.py

"""
Approach: Use a dictionary with key of the numbers spoken and values
of a list with two values consisting of the _last two turns_ when
that value was spoken. If it has only been spoken once, then the
index 0 value in the list is -1.
"""

def main():
    TARGET_TURN = 2020
    input = [1, 12, 0, 20, 8, 16]

    game = dict()
    for turn, num in enumerate(input):
        game[num] = [-1, turn + 1]   # [previous, latest]

    turn = len(input)
    latest = input[-1]
    while turn < TARGET_TURN:
        turn += 1
        if (latest not in game) or (game[latest][0] == -1):
            latest = 0
            game[latest] = [game[latest][1], turn]
        else:
            latest = game[latest][1] - game[latest][0]
            if (latest not in game):
                game[latest] = [-1, turn]
            else:
                game[latest] = [game[latest][1], turn]

    result = latest

    print("Last spoken number: " + str(result))

if __name__ == "__main__":
    main()