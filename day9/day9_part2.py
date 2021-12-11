from typing import Dict, FrozenSet, List, Callable, NewType, Set, Tuple, TypedDict
import sys
import copy
import math

Grid = NewType('Grid', Dict[Tuple[int, int], int])

Basin = NewType('Basin', Set[Tuple[int,int]])
BasinFS = NewType('BasinFS', FrozenSet[Tuple[int,int]])

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

def get_adjacent_coords(coord: Tuple[int,int], grid: Grid) -> List[Tuple[int,int]]:
    adjacent_coords: List[Tuple[int,int]] = []
    for offset in [(-1,0),(0,-1),(0,1),(1,0)]:
        adjacent_coord: Tuple[int,int] = (coord[0] + offset[0], coord[1] + offset[1])
        if adjacent_coord not in grid:
            continue
        adjacent_coords.append(adjacent_coord)  
    return adjacent_coords

def get_isolated_basins(board: Board):
    # Create a basic object for every non-9 height coordinate
    coords_to_basins: Dict[Tuple[int,int], Basin] = {}
    for r in range(0, board['rows']):
        for c in range(0, board['cols']):
            if board['grid'][(r,c)] == 9:
                continue
            coords_to_basins[(r,c)] = Basin({(r,c)})

    # Walk every neighbor of every of every coordinate and merge
    # basin objects if niether has height 9
    # (slightly inefficient, as we double-visit each pairing)
    for coord in coords_to_basins.keys():
        if board['grid'][coord] == 9:
            continue
        for other_coord in get_adjacent_coords(coord, board['grid']):
            if board['grid'][other_coord] == 9:
                continue
            if coords_to_basins[coord] is coords_to_basins[other_coord]:
                continue
            # Merge basins
            new_basin: Basin = Basin(coords_to_basins[coord].union(coords_to_basins[other_coord]))
            for coord_in_new_basin in new_basin:
                coords_to_basins[coord_in_new_basin] = new_basin

    # Identify unique basins
    # unique_basins_fs: Set[FrozenSet[Tuple[int,int]]]
    unique_basins: Set[BasinFS] = set()
    for basin in coords_to_basins.values():
        unique_basins.add(BasinFS(frozenset(basin)))
    return unique_basins

def get_product_of_largest_basin_sizes(board: Board) -> int:
    basins = get_isolated_basins(board)
    basins_ordered = list(basins)
    basins_ordered.sort(key=len, reverse=True)
    return math.prod(list(map(lambda basin: len(basin), basins_ordered[0:3])))
