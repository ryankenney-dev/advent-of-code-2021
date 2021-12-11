from typing import Dict, List, Callable, NewType, Set, Tuple, TypedDict
import sys

Grid = NewType('Grid', Dict[Tuple[int, int], int])

class Board(TypedDict):
    rows: int
    cols: int
    grid: Grid

def parse_board(message: str) -> Board:
    grid: Grid = Grid({})
    lines = message.splitlines()
    for r in range(0, len(lines)):
        row = lines[r]
        for c in range(0, len(row)):
            grid[(r,c)] = int(row[c])
    return {
        'rows': len(lines),
        'cols': len(lines[0]),
        'grid': grid,
    }

def get_adjacent_heights(coord: Tuple[int,int], grid: Grid) -> List[int]:
    adjacent_heights: List[int] = []
    for row_offset in [-1,0,1]:
        for col_offset in [-1,0,1]:
            if row_offset == 0 and col_offset == 0:
                continue
            adjacent_coord: Tuple[int,int] = (coord[0] + row_offset, coord[1] + col_offset)
            if adjacent_coord not in grid:
                continue
            adjacent_heights.append(grid[adjacent_coord])  
    return adjacent_heights

def get_low_point_heights(board: Board) -> List[int]:
    low_point_heights: List[int] = []
    for row in range(0, board['rows']):
        for col in range(0, board['cols']):
            coord = (row,col)
            height = board['grid'][coord]
            if height < min(get_adjacent_heights(coord, board['grid'])):
                low_point_heights.append(height)
    return low_point_heights

def get_sum_of_low_point_risk(board: Board) -> int:
    low_point_heights = get_low_point_heights(board)
    sum_of_risk: int = 0
    for low_point_height in low_point_heights:
        sum_of_risk += 1 + low_point_height
    return sum_of_risk
