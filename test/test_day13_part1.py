import day13.day13_part1 as puzzle
from typing import Dict, List, Optional, Set, Tuple
import unittest

class TestDay13Part1(unittest.TestCase):

    message: str ='''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''

    def test_parse_instructions(self):

        # Setup
        # ----
        board: puzzle.Board = puzzle.parse_instructions(self.message)
        expected_board: Set[Tuple[int,int]] = {
            'points': set({
                (6,10),
                (0,14),
                (9,10),
                (0,3),
                (10,4),
                (4,11),
                (6,0),
                (6,12),
                (4,1),
                (0,13),
                (10,12),
                (3,4),
                (3,0),
                (8,4),
                (1,10),
                (2,14),
                (8,10),
                (9,0),
            }),
            'folds': [
                ('y', 7),
                ('x', 5),
            ]
        }

        # Execute
        # ----
        board: puzzle.Board = puzzle.parse_instructions(self.message)

        # Verify
        # ----
        self.assertEqual(board, expected_board)

    def test_fold_board(self):

        # Setup
        # ----
        board: puzzle.Board = puzzle.parse_instructions(self.message)
        expected_boards: List[Set[Tuple[int,int]]] = [
            {
                'points': set({
                    (0,0), (2,0), (3,0), (6,0), (9,0),
                    (0,1), (4,1), 
                    (6,2), (10,2), 
                    (0,3), (4,3), 
                    (1,4), (3,4), (6,4), (8,4), (9,4), (10,4),
                }),
                'folds': [
                    ('x', 5),
                ]
            },{
                'points': set({
                    (0,0), (1,0), (2,0), (3,0), (4,0),
                    (0,1), (4,1),
                    (0,2), (4,2),
                    (0,3), (4,3),
                    (0,4), (1,4), (2,4), (3,4), (4,4),
                }),
                'folds': []
            }
        ]

        # Execute / Verify
        # ----
        puzzle.fold_board(board)
        self.assertEqual(board, expected_boards[0])
        puzzle.fold_board(board)
        self.assertEqual(board, expected_boards[1])
