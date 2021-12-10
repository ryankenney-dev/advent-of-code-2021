import day9.day9_part1 as puzzle
from typing import List
import unittest

class TestDay9Part1(unittest.TestCase):

    message: str ='''2199943210
3987894921
9856789892
8767896789
9899965678'''

    def test_parse_board(self):

        # Setup
        # ----
        expected_board: List[puzzle.Entry] = {
            'cols': 10,
            'rows': 5,
            'grid': {
                (0,0): 2, (0,1): 1, (0,2): 9, (0,3): 9, (0,4): 9, (0,5): 4, (0,6): 3, (0,7): 2, (0,8): 1, (0,9): 0,
                (1,0): 3, (1,1): 9, (1,2): 8, (1,3): 7, (1,4): 8, (1,5): 9, (1,6): 4, (1,7): 9, (1,8): 2, (1,9): 1,
                (2,0): 9, (2,1): 8, (2,2): 5, (2,3): 6, (2,4): 7, (2,5): 8, (2,6): 9, (2,7): 8, (2,8): 9, (2,9): 2, 
                (3,0): 8, (3,1): 7, (3,2): 6, (3,3): 7, (3,4): 8, (3,5): 9, (3,6): 6, (3,7): 7, (3,8): 8, (3,9): 9,
                (4,0): 9, (4,1): 8, (4,2): 9, (4,3): 9, (4,4): 9, (4,5): 6, (4,6): 5, (4,7): 6, (4,8): 7, (4,9): 8,
            }
        }

        # Execute
        # ----
        board: puzzle.Board = puzzle.parse_board(self.message)

        # Verify
        # ----
        self.assertEqual(board, expected_board)

    def test_get_adjacent_heights(self):

        # Setup
        # ----
        board: puzzle.Board = puzzle.parse_board(self.message)
        test_cases = [{
            'coord': (0,0),
            'expected_adjacents': [1, 3, 9]
        },{
            'coord': (2,5),
            'expected_adjacents': [8, 9, 4, 7, 9, 8, 9, 6]
        },{
            'coord': (4,9),
            'expected_adjacents': [8, 9, 7]
        }]

        # Execute / Verify
        # ----
        for test_case in test_cases:
            self.assertEqual(puzzle.get_adjacent_heights(test_case['coord'], board['grid']), test_case['expected_adjacents'])

    def test_get_low_point_heights(self):

        # Setup
        # ----
        board: puzzle.Board = puzzle.parse_board(self.message)
        expected_low_points = [1, 0, 5, 5]

        # Execute / Verify
        # ----
        self.assertEqual(puzzle.get_low_point_heights(board), expected_low_points)

    def test_get_sum_of_low_point_risk(self):

        # Setup
        # ----
        board: puzzle.Board = puzzle.parse_board(self.message)

        # Execute / Verify
        # ----
        self.assertEqual(puzzle.get_sum_of_low_point_risk(board), 15)

