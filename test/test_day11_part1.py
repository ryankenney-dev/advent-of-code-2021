import day11.day11_part1 as puzzle
from typing import Dict, List, Optional, Set
import unittest

class TestDay11Part1(unittest.TestCase):

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
            'flash_count': 0
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
        expected_boards: Dict[int, str] = {
            0: '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526''',
            1: '''6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637''',
            2: '''8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848''',
            100: '''0397666866
0749766918
0053976933
0004297822
0004229892
0053222877
0532222966
9322228966
7922286866
6789998766'''
        }

        # Execute / Verify
        # ----
        for round in range(0, max(expected_boards.keys())):
            if round in expected_boards:
                actual_board: str = puzzle.board_to_text(board)
                self.assertEqual(actual_board, expected_boards[round], 'Round [%s]' % str(round))
            puzzle.execute_round(board)

    def test_execute_round_flash_count(self):

        # Setup
        # ----
        board: puzzle.Board = puzzle.parse_board(self.message)

        # Execute
        # ----
        for round in range(0, 100):
            puzzle.execute_round(board)

        # Verify
        # ----
        self.assertEqual(board['flash_count'], 1656)

