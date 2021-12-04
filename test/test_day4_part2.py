import day4.day4_part2 as puzzle
from typing import List, TypedDict
import unittest

class TestDay4Part2(unittest.TestCase):

    message: str ='''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

    def test_parse_drawn_balls(self):

        # Setup
        # ----
        expected_parsed: List[int] = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
        
        # Execute
        # ----
        actual_parsed: List[int] = puzzle.parse_drawn_balls(self.message)

        # Verify
        # ----
        self.assertEqual(actual_parsed, expected_parsed)

    def test_parse_boards(self):

        # Setup
        # ----
        expected_parsed: List[int] = [
            [
                [22, 13, 17, 11,  0],
                [ 8,  2, 23,  4, 24],
                [21,  9, 14, 16,  7],
                [ 6, 10,  3, 18,  5],
                [ 1, 12, 20, 15, 19],
            ],[
                [ 3, 15,  0,  2, 22],
                [ 9, 18, 13, 17,  5],
                [19,  8,  7, 25, 23],
                [20, 11, 10, 24,  4],
                [14, 21, 16, 12,  6],
            ],[
                [14, 21, 17, 24,  4],
                [10, 16, 15,  9, 19],
                [18,  8, 23, 26, 20],
                [22, 11, 13,  6,  5],
                [ 2,  0, 12,  3,  7],
            ]
        ]
        
        # Execute
        # ----
        actual_parsed: List[int] = puzzle.parse_boards(self.message)

        # Verify
        # ----
        self.assertEqual(actual_parsed, expected_parsed)

    def test_is_winner_horizontal(self):

        class TestCase(TypedDict):
            board: puzzle.Board
            expected_winner: bool

        # Setup
        # ----
        test_cases: List[TestCase] = [{
            'board': [
                [None,None,None,None,   0],
                [None,None,None,None,   0],
                [None,None,None,None,   0],
                [None,None,None,None,   0],
                [None,None,None,None,   0]],
            'expected_winner': False,
        },{
            'board': [
                [None,None,None,None,   0],
                [None,None,None,   0,None],
                [None,None,   0,None,None],
                [None,   0,None,None,None],
                [   0,None,None,None,None]],
            'expected_winner': False,
        },{
            'board': [
                [None,None,None,None,None],
                [   0,   0,   0,   0,   0],
                [   0,   0,   0,   0,   0],
                [   0,   0,   0,   0,   0],
                [   0,   0,   0,   0,   0]],
            'expected_winner': True,
        },{
            'board': [
                [   0,   0,   0,   0,   0],
                [   0,   0,   0,   0,   0],
                [   0,   0,   0,   0,   0],
                [   0,   0,   0,   0,   0],
                [None,None,None,None,None]],
            'expected_winner': True,
        }]

        # Execute/Verify
        # ----
        test_case: TestCase = None
        for test_case in test_cases:
            actual_is_winner: bool = puzzle.is_winner_horizontal(test_case['board'])
            self.assertEqual(actual_is_winner, test_case['expected_winner'], msg="Test Case: %s" % test_case)

    def test_is_winner_vertical(self):

        class TestCase(TypedDict):
            board: puzzle.Board
            expected_winner: bool

        # Setup
        # ----
        test_cases: List[TestCase] = [{
            'board': [
                [None,None,None,None,None],
                [None,None,None,None,None],
                [None,None,None,None,None],
                [None,None,None,None,None],
                [   0,   0,   0,   0,   0]],
            'expected_winner': False,
        },{
            'board': [
                [None,None,None,None,   0],
                [None,None,None,   0,None],
                [None,None,   0,None,None],
                [None,   0,None,None,None],
                [   0,None,None,None,None]],
            'expected_winner': False,
        },{
            'board': [
                [None,   0,   0,   0,   0],
                [None,   0,   0,   0,   0],
                [None,   0,   0,   0,   0],
                [None,   0,   0,   0,   0],
                [None,   0,   0,   0,   0]],
            'expected_winner': True,
        },{
            'board': [
                [   0,   0,   0,   0,None],
                [   0,   0,   0,   0,None],
                [   0,   0,   0,   0,None],
                [   0,   0,   0,   0,None],
                [   0,   0,   0,   0,None]],
            'expected_winner': True,
        }]

        # Execute/Verify
        # ----
        test_case: TestCase = None
        for test_case in test_cases:
            actual_is_winner: bool = puzzle.is_winner_vertical(test_case['board'])
            self.assertEqual(actual_is_winner, test_case['expected_winner'], msg="Test Case: %s" % test_case)

    def test_sum_of_unmarked_squares(self):
        
        # Setup
        # ----
        board: puzzle.Board = [
            [None,None,None,None,None],
            [  10,  16,  15,None,  19],
            [  18,   8,None,  26,  20],
            [  22,None,  13,   6,None],
            [None,None,  12,   3,None]
        ]

        # Execute
        # ----
        sum: int = puzzle.sum_of_unmarked_squares(board)

        # Verify
        # ----
        self.assertEqual(sum, 188)

    def test_find_last_winning_board_score(self):

        # Execute
        # ----
        balls: List[int] = puzzle.parse_drawn_balls(self.message)
        boards: List[puzzle.Board] = puzzle.parse_boards(self.message)
        score: int = puzzle.find_last_winning_board_score(balls, boards)

        # Verify
        # ----
        self.assertEqual(score, 1924)
