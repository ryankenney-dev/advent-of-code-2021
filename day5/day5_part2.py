from typing import Any, List, NewType, Tuple, TypedDict, Match, Optional
import copy
import re

class Point(TypedDict):
    row: int
    col: int

Line = NewType('Line', List[Point])

Diagram = NewType('Diagram', List[List[int]])

def parse_lines(message: str) -> List[Line]:
    text_lines: List[str] = message.splitlines()
    lines: List[Line] = []
    text_line: str
    for text_line in text_lines:
        pattern: re.Pattern = re.compile('^(\d+),(\d+) -> (\d+),(\d+)$')
        text_line_parts: Optional[re.Match[str]] = pattern.search(text_line)
        # NOTE: This line automatically re-types the variable from Optional[re.Match[str]] to re.Match[str],
        # which clears the following typing error:
        #   Item "None" of "Optional[Match[str]]" has no attribute "group"
        assert text_line_parts is not None
        lines.append(Line([
            {'row': int(text_line_parts.group(2)), 'col': int(text_line_parts.group(1))},
            {'row': int(text_line_parts.group(4)), 'col': int(text_line_parts.group(3))},
        ]))
    return lines

def render_diagram(lines: List[Line]) -> Diagram:
    diagram: Diagram = create_empty_diagram(lines)
    for line in lines:
        end = line[1]
        coord: Point = line[0]
        diagram[coord['row']][coord['col']] += 1
        while coord != end:
            coord = increment_coordindate(coord, end)
            diagram[coord['row']][coord['col']] += 1
    return diagram        

def increment_coordindate(from_point: Point, to_point: Point) -> Point:
    increment: Point = {'row': 0, 'col': 0}
    if to_point['row'] > from_point['row']:
        increment['row'] = 1
    elif to_point['row'] < from_point['row']:
        increment['row'] = -1
    if to_point['col'] > from_point['col']:
        increment['col'] = 1
    elif to_point['col'] < from_point['col']:
        increment['col'] = -1
    return {'row': from_point['row']+increment['row'], 'col': from_point['col']+increment['col']}

def create_empty_diagram(lines: List[Line]) -> Diagram:
    # NOTE: We assume coords non-negative
    max_coord: Point = {'row': 0, 'col': 0}
    for line in lines:
        max_coord['row'] = max(max_coord['row'], line[0]['row'], line[1]['row'])
        max_coord['col'] = max(max_coord['col'], line[0]['col'], line[1]['col'])
    board_row: List[int] = [0] * (max_coord['col']+1)
    board: List[List[int]] = []
    for i in range(0, max_coord['row']+1):
        board.append(copy.deepcopy(board_row))
    return Diagram(board)

def count_danger_points(diagram: Diagram) -> int:
    danger_points: int = 0
    for row in diagram:
        for value in row:
            if value > 1:
                danger_points += 1
    return danger_points
