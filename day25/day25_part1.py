from typing import Dict, FrozenSet, List, Callable, NewType, Optional, Set, Tuple, TypedDict
import copy

class State(TypedDict):
    eastern_cucumbers: Set[Tuple[int,int]]
    southern_cucumbers: Set[Tuple[int,int]]
    bounds: Tuple[int,int]

def parse_input(message: str) -> State:
    eastern_cucumbers: Set[Tuple[int,int]] = set()
    southern_cucumbers: Set[Tuple[int,int]]  = set()
    lines = message.splitlines()
    for row in range(0, len(lines)):
        for col in range(0, len(lines[0])):
            c: str = lines[row][col]
            if c == '.':
                continue
            elif c == '>':
                eastern_cucumbers.add((row,col))
            elif c == 'v':
                southern_cucumbers.add((row,col))
            else:
                raise Exception('Invalid character: %s' % c)
    return {
        'eastern_cucumbers': eastern_cucumbers,
        'southern_cucumbers': southern_cucumbers,
        'bounds': (len(lines),len(lines[0])),
    }

def run_cycle(state: State) -> None:
    (bounds_rows,bounds_cols) = state['bounds']
    moved_coord: Tuple[int,int]
    moved_coords: Set[Tuple[int,int]]

    moved_coords = set()
    for coord in state['eastern_cucumbers']:
        moved_coord = (coord[0], (coord[1]+1)%bounds_cols)
        if moved_coord in state['southern_cucumbers'] or \
            moved_coord in state['eastern_cucumbers']:
            moved_coords.add(coord)
        else:
            moved_coords.add(moved_coord)

    state['eastern_cucumbers'] = moved_coords

    moved_coords = set()
    for coord in state['southern_cucumbers']:
        moved_coord = ((coord[0]+1)%bounds_rows, coord[1])
        if moved_coord in state['southern_cucumbers'] or \
            moved_coord in state['eastern_cucumbers']:
            moved_coords.add(coord)
        else:
            moved_coords.add(moved_coord)

    state['southern_cucumbers'] = moved_coords

def run_cycles_until_stable(state: State) -> int:
    i: int = 0
    while True:
        last_state = copy.deepcopy(state)
        run_cycle(state)
        i += 1
        if state == last_state:
            break
    return i

def state_to_string(state: State): 
    (bounds_rows,bounds_cols) = state['bounds']
    lines: List[str] = []
    for row in range(0, bounds_rows):
        line: List[str] = []
        for col in range(0, bounds_cols):
            c: str
            if (row,col) in state['eastern_cucumbers']:
                c = '>'
            elif (row,col) in state['southern_cucumbers']:
                c = 'v'
            else:
                c = '.'
            line.append(c)
        lines.append(''.join(line))
    return '\n'.join(lines)