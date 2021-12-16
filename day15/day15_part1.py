from typing import Dict, FrozenSet, List, Callable, NewType, Optional, Set, Tuple, TypedDict
import re
import sys
import copy

Coord = Tuple[int,int]
Grid = Dict[Coord, int]

class State(TypedDict):
    # Map of coords to risk values from the input
    coord_risks: Grid
    # Map of coords to total risk to coord
    coord_cumulative_risks: Grid
    # Coord of the initial location
    start_coord: Coord
    # Coord of the final location
    end_coord: Coord

def parse_input(message: str) -> State:
    coord_risks: Grid = {}
    lines = message.splitlines()
    for row in range(0, len(lines)):
        for col in range(0, len(lines[0])):
            coord_risks[(row,col)] = int(lines[row][col])
    return {
        'coord_risks': coord_risks,
        'coord_cumulative_risks': {},
        'start_coord': (0,0),
        'end_coord': (row,col),
    }

def walk_routes(state: State, cumulative_risk: int, path: List[Coord]) -> Optional[Tuple[int, List[Coord]]]:

    if path[-1] == state['end_coord']:
        return (cumulative_risk, path)

    best_result: Optional[Tuple[int, List[Coord]]] = None

    # Store lowest risk seen to each coord, stop if longer
    adjacent_coords: List[Tuple[int,int]] = get_adjacent_coords(path[-1], state['coord_risks'])
    for adjacent_coord in adjacent_coords:

        if adjacent_coord == state['start_coord']:
            # Never return to the start
            continue

        if adjacent_coord in path:
            # We've already visited this point, so stop (risk can only increase)
            continue

        state['coord_cumulative_risks'].setdefault(adjacent_coord, sys.maxsize)
        adjacent_cumulative_risk: int = cumulative_risk + state['coord_risks'][adjacent_coord]
        if adjacent_cumulative_risk >= state['coord_cumulative_risks'][adjacent_coord]:
            # We've seen a lower risk route to this coord, so stop
            continue
        state['coord_cumulative_risks'][adjacent_coord] = adjacent_cumulative_risk

        adjacent_path = copy.copy(path)
        adjacent_path.append(adjacent_coord)

        result: Optional[Tuple[int, List[Coord]]] = walk_routes(state, adjacent_cumulative_risk, adjacent_path)
        if result is None:
            continue
        if best_result is None:
            best_result = result
            continue
        if best_result[0] < result[0]:
            continue
        best_result = result

    return best_result

def get_adjacent_coords(coord: Tuple[int,int], grid: Grid) -> List[Tuple[int,int]]:
    adjacent_coords: List[Tuple[int,int]] = []
    for offset in [(1,0),(0,1),(0,-1),(-1,0)]:
        adjacent_coord: Tuple[int,int] = (coord[0] + offset[0], coord[1] + offset[1])
        if adjacent_coord not in grid:
            continue
        adjacent_coords.append(adjacent_coord)  
    return adjacent_coords
