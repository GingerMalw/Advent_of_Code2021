import numpy
from pathlib import Path


class Board:
    def __init__(self):
        self.board = numpy.zeros((5, 5), dtype=int)
        self.marked = numpy.zeros((5, 5))

    def read_from_lines(self, lines):
        for i in range(5):
            line_entries = [int(entry) for entry in lines[i].split(" ") if entry != " "]
            self.board[i] = line_entries


datas = Path('Day 4 - bingo input')
with datas.open(mode='r') as f:
    # reading file line by line (useful)
    lines = [entry.strip() for entry in f.readlines()]
print(lines)

pl_numbers = [int(entry) for entry in lines[0].split(",")]
print(pl_numbers)

nr_boards = (len(lines)-1)/6
print(f"There is {nr_boards} boards.")

boards = dict()
for b in range(int(nr_boards)):
    boards[b] = Board()
    boards[b].read_from_lines(lines[(2 + b*6):(2 + 5 + (b+1)*6)])

