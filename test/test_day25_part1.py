from unittest.case import expectedFailure
import day25.day25_part1 as puzzle
from typing import Dict, List, Optional, Set, Tuple
import unittest

class TestDay25Part1(unittest.TestCase):

    message: str ='''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>'''

    def test_parse_input(self):

        # Setup
        # ----
        message: str ='''..........
.>v....v..
.......>..
..........'''
        expected_state: puzzle.State = {
            'eastern_cucumbers': { (1,1),(2,7) },
            'southern_cucumbers': { (1,2),(1,7) },
            'bounds': (4,10)
        }

        # Execute
        # ----
        state: puzzle.State = puzzle.parse_input(message)

        # Verify
        # ----
        self.assertEqual(state, expected_state)

    def test_state_to_string(self):

        # Setup
        # ----
        message: str ='''..........
.>v....v..
.......>..
..........'''
        state: puzzle.State = puzzle.parse_input(message)

        # Execute
        # ----
        output: str = puzzle.state_to_string(state)

        # Verify
        # ----
        self.assertEqual(message, output)

    def test_run_cycle(self):

        # Setup
        # ----
        state: puzzle.State = puzzle.parse_input(self.message)
        expected_states: str = {
            0: '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>''',
            1: '''....>.>v.>
v.v>.>v.v.
>v>>..>v..
>>v>v>.>.v
.>v.v...v.
v>>.>vvv..
..v...>>..
vv...>>vv.
>.v.v..v.v''',
            58: '''..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv.....>>
>vv......>
.>v.vv.v..''',
        }

        # Execute / Verify
        # ----
        for i in range(0, 60):
            if i in expected_states:
                self.assertEqual(puzzle.state_to_string(state), expected_states[i], 'Cycle: %s' % i)
            puzzle.run_cycle(state)

    def test_run_cycles_until_stable(self):

        # Setup
        # ----
        state: puzzle.State = puzzle.parse_input(self.message)

        # Execute
        # ----
        cycles: int = puzzle.run_cycles_until_stable(state)

        # Verify
        # ----
        self.assertEqual(cycles, 58)
