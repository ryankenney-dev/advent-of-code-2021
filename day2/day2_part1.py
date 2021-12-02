from typing import List, NewType, TypedDict, Tuple
import copy

class SubCommand(TypedDict):
    action: str
    value: int

def parse_input(message: str) -> List[SubCommand]:
    return list(map(lambda line: parse_input_line(line), message.splitlines()))

def parse_input_line(line: str) -> SubCommand:
    line_parts = line.split(' ')
    return SubCommand(action=line_parts[0], value=int(line_parts[1]))

class Position(TypedDict):
    horizontal: int
    depth: int

def compute_position(commands: List[SubCommand]) -> Position:
    horizontal: int = 0
    depth: int = 0
    for command in commands:
        if command['action'] == 'forward':
            horizontal += command['value']
        elif command['action'] == 'up':
            depth -= command['value']
        elif command['action'] == 'down':
            depth += command['value']
        else:
            raise Exception('Unrecognized action [%s]' % command['action'])
    return Position(horizontal=horizontal, depth=depth)
