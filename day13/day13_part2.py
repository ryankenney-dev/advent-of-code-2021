from typing import Dict, FrozenSet, List, Callable, NewType, Optional, Set, Tuple, TypedDict
import re
import sys

class Board(TypedDict):
    points: Set[Tuple[int,int]]
    folds: List[Tuple[str, int]]

def parse_instructions(message: str) -> Board:
    matcher = re.compile(r'^\d+,\d+$')
    points: Set[Tuple[int,int]] = set()
    lines: List[str] = message.splitlines()
    while len(lines) > 0:
        line = lines.pop(0)
        if line == '':
            break
        coord_parts = line.split(',')
        points.add((int(coord_parts[0]), int(coord_parts[1])))
    folds: List[Tuple[str,int]] = []
    while len(lines) > 0:
        line = lines.pop(0)
        value: str = line[len('fold along .='):]
        if line.startswith('fold along x='):
            folds.append(('x', int(value)))
        else:
            folds.append(('y', int(value)))
    return {
        'points': points,
        'folds': folds,
    }

def fold_board(board: Board) -> None:
    fold_dir: str; fold_dist: int;
    (fold_dir, fold_dist) = board['folds'].pop(0)
    new_points: Set[Tuple[int,int]] = set()
    x: int; y: int;
    for (x,y) in board['points']:
        if (fold_dir == 'x' and x <= fold_dist) or \
            (fold_dir == 'y' and y <= fold_dist):
                new_points.add((x,y))
                continue
        if fold_dir == 'x':
            x = fold_dist - (x - fold_dist)
        else:
            y = fold_dist - (y - fold_dist)
        new_points.add((x, y))
    board['points'] = new_points

def get_coord_bounds(board: Board) -> Tuple[int,int]:
    x_max: int = 0; y_max: int = 0; 
    x: int; y: int;
    for (x,y) in board['points']:
        x_max = max(x, x_max); y_max = max(y, y_max);
    return (x_max+1, y_max+1)

def board_to_string(board: Board) -> str:
    max_x: int; max_y: int;
    (max_x, max_y) = get_coord_bounds(board)
    lines: List[str] = []
    for y in range(0, max_y):
        line: List[str] = []
        for x in range(0, max_x):
            if (x,y) in board['points']:
                line.append('#')
            else:
                line.append('.')
        lines.append(''.join(line))
    return '\n'.join(lines)
                