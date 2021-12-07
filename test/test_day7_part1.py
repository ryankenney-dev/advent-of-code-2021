import day7.day7_part1 as puzzle
from typing import List
import unittest

class TestDay7Part1(unittest.TestCase):

    message: str ='16,1,2,0,4,2,7,1,2,14'

    def test_parse_fish_times(self):

        # Setup
        # ----
        expected_positions: puzzle.Positions = [16,1,2,0,4,2,7,1,2,14]

        # Execute
        # ----
        positions: puzzle.Positions = puzzle.parse_positions(self.message)

        # Verify
        # ----
        self.assertEqual(positions, expected_positions)

    def test_find_cost_cheapest_position(self):

        # Setup
        # ----
        test_cases = {
            'positions': [16,1,2,0,4,2,7,1,2,14],
            'expected_cost': 37,
        },{
            'positions': [1,3,2,2,6,2,7,1,5],
            'expected_cost': 15,
        },{
            'positions': [2,5,2,2,6,3,9,9,7],
            'expected_cost': 22,
        },{
            'positions': [2,8,9,5,7,9,1,8,9],
            'expected_cost': 20,
        }

        # Execute and Verify
        # ----
        for test_case in test_cases:
            self.assertEqual(puzzle.find_cost_cheapest_position(test_case['positions']), test_case['expected_cost'])
