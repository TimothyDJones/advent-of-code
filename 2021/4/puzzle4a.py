# puzzle4a.py
from utils import *
from pprint import pprint, pformat

class Board(object):
    def __init__(self, board):
        self.board = map(str.split, board.splitlines())
        self.board = list(map(nums, self.board))
        self.rows = tuple(map(set, self.board))
        self.cols = tuple(map(set, zip(*self.board)))
        self.winner = False

    def check_winner(self, nums_called):
        for line in ((self.rows) + (self.cols)):
            if line.issubset(set(nums_called)):
                self.winner = True
                break
        return self.winner

    def sum_unmarked_nums(self, nums_called):
        sum_unmarked = 0
        for row in self.rows:
            sum_unmarked += sum(row.difference(set(nums_called)))
        return (sum_unmarked)

def main():
    (numbers, *boards) = read_input_from_file(filename="input4a.txt",
        datatype=str, sep="\n\n")
    numbers = list(map(int, numbers.split(",")))
    boards = [Board(board) for board in boards]

    nums_called = set()
    final_score = 0
    for i in range(len(numbers)):
        nums_called.add(numbers[i])
        for j in range(len(boards)):
            if boards[j].check_winner(nums_called):
                final_score = (boards[j].sum_unmarked_nums(nums_called)
                    * numbers[i])
                print("Board: {b}\nNumbers called: {n}\n"
                    "Last number called: {l}\nFinal score: {s}\n".
                    format(b=pformat(object=boards[j].board, indent=2),
                    n=nums_called, l=numbers[i], s=final_score))
                exit(0)

if __name__ == "__main__":
    main()