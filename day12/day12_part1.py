from typing import Dict, FrozenSet, List, Callable, NewType, Optional, Set, Tuple, TypedDict
import re
import sys

Grid = NewType('Grid', Dict[Tuple[int, int], int])

class Board(TypedDict):
    rows: int
    cols: int
    grid: Grid
    rounds: int

def parse_connections(message: str) -> Dict[str, List[str]]:
    connections: Dict[str, List[str]] = {}
    lines = message.splitlines()
    for line in lines:
        parts = line.split('-')
        add_to_multi_value_dict(connections, parts[0], parts[1])
        add_to_multi_value_dict(connections, parts[1], parts[0])
    return connections

def add_to_multi_value_dict(dict: Dict[str, List[str]], key, value) -> None:
    dict.setdefault(key, [])
    entry_list = dict.get(key)
    assert entry_list is not None
    entry_list.append(value)

def is_small_cave(cave: str) -> bool:
    if cave == 'start' or cave == 'end':
        return False
    return bool(re.compile(r'^[a-z]+$').match(cave))

def get_all_routes_inner(connections: Dict[str, List[str]], current_path: List[str]) -> List[List[str]]:
    completed_paths: List[List[str]] = []
    next_caves: Optional[List[str]] = connections[current_path[-1]]
    assert next_caves is not None
    for next_cave in next_caves:
        # Stop route search if small cave already in path
        if is_small_cave(next_cave) and next_cave in current_path:
            continue
        # Never return to the start
        if 'start' == next_cave:
            continue
        if 'end' == next_cave:
            completed_paths.append(current_path + [next_cave])
            continue
        completed_paths.extend(get_all_routes_inner(connections, current_path + [next_cave]))
    return completed_paths

def get_all_routes(connections: Dict[str, List[str]]) -> Set[Tuple[str,...]]:
    routes_set: Set[Tuple[str,...]] = set()
    routes_list: List[List[str]] = get_all_routes_inner(connections, ['start'])
    for route in routes_list:
        routes_set.add(tuple(route))
    return routes_set

