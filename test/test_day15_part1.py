from unittest.case import expectedFailure
import day15.day15_part1 as puzzle
from typing import Dict, List, Optional, Set, Tuple
import unittest

class TestDay15Part1(unittest.TestCase):

    message: str ='''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''

    def test_parse_input(self):

        # Setup
        # ----
        message = '''116
138'''
        expected_state: puzzle.State = {
            'coord_risks': {
                (0,0): 1, (0,1): 1, (0,2): 6,
                (1,0): 1, (1,1): 3, (1,2): 8,
            },
            'coord_cumulative_risks': {},
            'start_coord': (0,0),
            'end_coord': (1,2),
        }
        # Execute / Verify
        # ----
        state: puzzle.State = puzzle.parse_input(message)

        # Verify
        # ----
        self.assertEqual(state, expected_state)

    def test_walk_routes(self):

        # Setup
        # ----
        state: puzzle.State = puzzle.parse_input(self.message)
        expected_route = (
            40,
            [
                (0,0),
                (1,0),
                (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6),
                (3,6), (3,7),
                (4,7),
                (5,7), (5,8),
                (6,8),
                (7,8),
                (8,8), (8,9),
                (9,9),
            ]
        )

        # Execute / Verify
        # ----
        route = puzzle.walk_routes(state, 0, [(0,0)])

        # Verify
        # ----
        self.assertEqual(route, expected_route)
