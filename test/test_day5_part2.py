import day5.day5_part2 as puzzle
from typing import List
import unittest

class TestDay5Part1(unittest.TestCase):

    message: str ='''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''

    def test_parse_lines(self):

        # Setup
        # ----
        expected_lines: List[puzzle.Line] = [
            [{'col': 0, 'row': 9},{'col': 5, 'row': 9}],
            [{'col': 8, 'row': 0},{'col': 0, 'row': 8}],
            [{'col': 9, 'row': 4},{'col': 3, 'row': 4}],
            [{'col': 2, 'row': 2},{'col': 2, 'row': 1}],
            [{'col': 7, 'row': 0},{'col': 7, 'row': 4}],
            [{'col': 6, 'row': 4},{'col': 2, 'row': 0}],
            [{'col': 0, 'row': 9},{'col': 2, 'row': 9}],
            [{'col': 3, 'row': 4},{'col': 1, 'row': 4}],
            [{'col': 0, 'row': 0},{'col': 8, 'row': 8}],
            [{'col': 5, 'row': 5},{'col': 8, 'row': 2}]]        

        # Execute
        # ----
        lines: List[puzzle.Line] = puzzle.parse_lines(self.message)

        # Verify
        # ----
        self.assertEqual(expected_lines, lines)

    def test_create_empty_diagram(self):

        # Setup
        # ----
        lines: List[puzzle.Line] = puzzle.parse_lines(self.message)
        expected_diagram: puzzle.Diagram = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]

        # Execute
        # ----
        diagram: puzzle.Diagram = puzzle.create_empty_diagram(lines)

        # Verify
        # ----
        self.assertEqual(diagram, expected_diagram)

    def test_render_diagram(self):

        # Setup
        # ----
        lines: List[puzzle.Line] = puzzle.parse_lines(self.message)
        expected_diagram: puzzle.Diagram = [
            [1,0,1,0,0,0,0,1,1,0],
            [0,1,1,1,0,0,0,2,0,0],
            [0,0,2,0,1,0,1,1,1,0],
            [0,0,0,1,0,2,0,2,0,0],
            [0,1,1,2,3,1,3,2,1,1],
            [0,0,0,1,0,2,0,0,0,0],
            [0,0,1,0,0,0,1,0,0,0],
            [0,1,0,0,0,0,0,1,0,0],
            [1,0,0,0,0,0,0,0,1,0],
            [2,2,2,1,1,1,0,0,0,0]]

        # Execute
        # ----
        diagram: puzzle.Diagram = puzzle.render_diagram(lines)

        # Verify
        # ----
        self.assertEqual(diagram, expected_diagram)

    def test_count_danger_points(self):

        # Setup
        # ----
        lines: List[puzzle.Line] = puzzle.parse_lines(self.message)
        diagram: puzzle.Diagram = puzzle.render_diagram(lines)

        # Execute
        # ----
        danger_points: int = puzzle.count_danger_points(diagram)

        # Verify
        # ----
        self.assertEqual(danger_points, 12)

