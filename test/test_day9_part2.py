import day9.day9_part2 as puzzle
from typing import List, Set
import unittest

class TestDay9Part2(unittest.TestCase):

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

    def test_get_adjacent_coords(self):

        # Setup
        # ----
        board: puzzle.Board = puzzle.parse_board(self.message)
        test_cases = [{
            'coord': (0,0),
            'expected_adjacents': [(0,1), (1,0)]
        },{
            'coord': (2,5),
            'expected_adjacents': [(1,5), (2,4), (2,6), (3,5)]
        },{
            'coord': (4,9),
            'expected_adjacents': [(3,9), (4,8)]
        }]

        # Execute / Verify
        # ----
        for test_case in test_cases:
            self.assertEqual(puzzle.get_adjacent_coords(test_case['coord'], board['grid']), test_case['expected_adjacents'])

    def test_get_isolated_basins(self):

        # Setup
        # ----
        board: puzzle.Board = puzzle.parse_board(self.message)
        expected_small_basin: puzzle.BasinFS = {(0,0),(0,1),(1,0)}

        # Execute
        # ----
        basins: Set[puzzle.BasinFS] = puzzle.get_isolated_basins(board)

        # Verify
        # ----
        self.assertTrue(expected_small_basin in basins)
        self.assertEqual(len(basins), 4)

    def test_get_product_of_largest_basin_sizes(self):

        # Setup
        # ----
        board: puzzle.Board = puzzle.parse_board(self.message)

        # Execute / Verify
        # ----
        self.assertEqual(puzzle.get_product_of_largest_basin_sizes(board), 1134)
