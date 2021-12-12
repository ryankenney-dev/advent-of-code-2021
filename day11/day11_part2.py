from typing import Dict, List, Callable, NewType, Optional, Set, Tuple, TypedDict
import sys

Grid = NewType('Grid', Dict[Tuple[int, int], int])

class Board(TypedDict):
    rows: int
    cols: int
    grid: Grid
    rounds: int

def parse_board(message: str) -> Board:
    grid: Grid = Grid({})
    lines = message.splitlines()
    for r in range(0, len(lines)):
        row = lines[r]
        for c in range(0, len(row)):
            grid[(r,c)] = int(row[c])
    return Board({
        'rows': len(lines),
        'cols': len(lines[0]),
        'grid': grid,
        'rounds': 0,
    })

def execute_rounds_until_all_flash(board: Board) -> None:
    while True:
        flashes: int = execute_round(board)
        board['rounds'] += 1
        if flashes == len(board['grid']):
            break

def execute_round(board: Board) -> int:

    grid: Grid = board['grid']
    # Queue of point flashes that need to be processed
    flash_point_queue: List[Tuple[int,int]] = []
    # All points that flashed this round
    flash_points: Set[Tuple[int,int]] = set()

    # Increment all coords, adding >10 coods to flash_points
    coord: Tuple[int,int]
    for coord in grid:
        grid[coord] += 1
        if grid[coord] > 9:
            flash_point_queue.append(coord)
            flash_points.add(coord)

    # Affect neighbors of each flash point
    while len(flash_point_queue) > 0:
        coord = flash_point_queue.pop()
        adjacent_coords: List[Tuple[int,int]] = get_adjacent_coords(coord, grid)
        for adjacent_coord in adjacent_coords:
            grid[adjacent_coord] += 1
            # Queue any newly flashing
            if grid[adjacent_coord] > 9 and adjacent_coord not in flash_points:
                flash_point_queue.append(adjacent_coord)
                flash_points.add(adjacent_coord)

    # Reset all flashed points to 0
    for coord in flash_points:
        grid[coord] = 0

    return len(flash_points)

def get_adjacent_coords(coord: Tuple[int,int], grid: Grid) -> List[Tuple[int,int]]:
    adjacent_coords: List[Tuple[int,int]] = []
    for row_offset in [-1,0,1]:
        for col_offset in [-1,0,1]:
            if row_offset == 0 and col_offset == 0:
                continue
            adjacent_coord: Tuple[int,int] = (coord[0] + row_offset, coord[1] + col_offset)
            if adjacent_coord not in grid:
                continue
            adjacent_coords.append(adjacent_coord)  
    return adjacent_coords

def board_to_text(board: Board) -> str:
    rows: List[str] = []
    for r in range(0, board['rows']):
        row: List[str] = []
        for c in range(0, board['cols']):
            row.append(str(board['grid'][(r,c)]))
        rows.append(''.join(row))
    return '\n'.join(rows)