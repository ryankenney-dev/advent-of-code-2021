import day11.day11_part2 as puzzle
from typing import Dict, List, Optional, Set
import unittest

class TestDay11Part2(unittest.TestCase):

    message: str ='''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

    def test_parse_board(self):

        # Setup
        # ----
        message: str ='''2199
3987
9856'''
        expected_board: List[puzzle.Entry] = {
            'cols': 4,
            'rows': 3,
            'grid': {
                (0,0): 2, (0,1): 1, (0,2): 9, (0,3): 9,
                (1,0): 3, (1,1): 9, (1,2): 8, (1,3): 7,
                (2,0): 9, (2,1): 8, (2,2): 5, (2,3): 6,
            },
            'rounds': 0
        }

        # Execute
        # ----
        board: puzzle.Board = puzzle.parse_board(message)

        # Verify
        # ----
        self.assertEqual(board, expected_board)

    def test_get_adjacent_coords(self):

        # Setup
        # ----
        board: puzzle.Board = puzzle.parse_board(self.message)
        test_cases = [{
            'coord': (0,0),
            'expected_adjacents': [(0,1), (1,0), (1,1)]
        },{
            'coord': (2,5),
            'expected_adjacents': [(1,4), (1,5), (1,6), (2,4), (2,6), (3,4), (3,5), (3,6)]
        },{
            'coord': (9,9),
            'expected_adjacents': [(8,8), (8,9), (9,8)]
        }]

        # Execute / Verify
        # ----
        for test_case in test_cases:
            self.assertEqual(puzzle.get_adjacent_coords(test_case['coord'], board['grid']), test_case['expected_adjacents'])

    def test_execute_round(self):

        # Setup
        # ----
        board: puzzle.Board = puzzle.parse_board(self.message)

        # Execute
        # ----
        puzzle.execute_rounds_until_all_flash(board)

        # Verify
        # ----
        self.assertEqual(board['rounds'], 195)

