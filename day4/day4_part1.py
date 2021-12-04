from typing import List, Optional
import copy
import re

Board = List[List[Optional[int]]]

def parse_drawn_balls(message: str) -> List[int]:
    lines: List[str] = message.splitlines()
    return list(map(lambda s: int(s), lines[0].split(',')))

def parse_boards(message: str) -> List[Board]:
    lines: List[str] = message.splitlines()
    boards: List[Board] = []
    current_board = List[List[int]]
    # Skip the first line
    lines.pop(0)
    for line in lines:
        if line == '':
            board: Board = []
            boards.append(board)
            continue
        row: List[Optional[int]] = list(map(lambda s: int(s), re.split('\s+', line.strip())))
        board.append(row)
    return boards

def find_winning_board_score(balls: List[int], boards: List[Board]) -> int:
    boards = copy.deepcopy(boards)

    winning_board: Optional[Board] = None
    for ball in balls:

        # Mark matching squares
        for board in boards:
            for row in board:
                for x in range(0, len(row)):
                    if row[x] != ball:
                        continue
                    row[x] = None

        # Look for winning board
        for board in boards:
            if is_winner_horizontal(board) or is_winner_vertical(board):
                winning_board = board
                break

        if winning_board is not None:
            break

    if winning_board is None:
        raise Exception('No winner found')

    # Compute score
    return ball * sum_of_unmarked_squares(winning_board)

def sum_of_unmarked_squares(board: Board) -> int:
    sum: int = 0
    row: List[Optional[int]]; value: Optional[int]
    for row in board:
        for value in row:
            if value is None:
                continue
            sum += value
    return sum

def is_winner_horizontal(board: Board) -> bool:
    row: int; col: int
    for row in range(0, len(board)):
        all_values_marked: bool = True
        for col in range(0, len(board[0])):
            if board[row][col] is not None:
                all_values_marked = False
                break
        if all_values_marked:
            return True
    return False

def is_winner_vertical(board: Board) -> bool:
    row: int; col: int
    for col in range(0, len(board[0])):
        all_values_marked: bool = True
        for row in range(0, len(board)):
            if board[row][col] is not None:
                all_values_marked = False
                break
        if all_values_marked:
            return True
    return False
