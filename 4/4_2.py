import enum
from re import T
import re
from typing import List

BOARD_SIZE = 5


class Board:
    def __init__(self, lines: List[str]) -> None:
        if len(lines) != 5:
            raise Exception("lines should be len 5")

        self.fields = [[0 for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]
        self.marked = [[False for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

        for row, line in enumerate(lines):
            line = line.replace("\n", "").replace("  ", " ")
            if line[0] == " ":
                line = line[1:]
            vals = line.split(" ")
            for col, v in enumerate(vals):
                self.fields[row][col] = int(v)

    def __str__(self) -> str:
        s = ""
        for i, rows in enumerate(self.fields):
            for j, col in enumerate(rows):
                s += f"{col} {self.marked[i][j]} "
            s += "\n"
        return s

    def mark(self, number: int):
        for i, row in enumerate(self.fields):
            for j, value in enumerate(row):
                if value == number:
                    self.marked[i][j] = True

    def is_solved(self) -> bool:
        # row by row.
        for row in self.marked:
            if False not in row:
                return True

        # col by col.
        for i in range(BOARD_SIZE):
            solved = True
            for row in self.marked:
                solved &= row[i]
            if solved:
                return True

        return False

    def sum_of_unmarked(self) -> int:
        sum = 0
        for i, rows in enumerate(self.marked):
            for j, marked in enumerate(rows):
                if not marked:
                    sum += self.fields[i][j]
        return sum


def lines_to_boards(lines: List[str]) -> List[Board]:
    boards = []
    while len(lines) != 0:
        if lines[0] == "\n":
            lines = lines[1:]
        take = lines[:5]
        boards.append(Board(take))
        lines = lines[5:]

    return boards


def filter_out_solved(boards: List[Board]) -> List[Board]:
    new = []
    for board in boards:
        if not board.is_solved():
            new.append(board)

    return new


with open("input.txt") as f:
    numbers = f.readline()

    lines = f.readlines()

    boards = lines_to_boards(lines)
    not_solved = len(boards)

    for number in numbers.split(","):
        num = int(number)
        for i, board in enumerate(boards):
            if board.is_solved():
                continue
            board.mark(num)
            if board.is_solved():
                not_solved -= 1
                if not_solved == 0:
                    print(f"board: {i}, num: {num}")
                    print(board.sum_of_unmarked() * num)
