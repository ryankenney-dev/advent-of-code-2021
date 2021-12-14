import day14.day14_part1 as puzzle
from typing import Dict, List, Optional, Set, Tuple
import unittest

class TestDay14Part1(unittest.TestCase):

    message: str ='''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''

    def test_run_polymer_step(self):

        # Setup
        # ----
        state: puzzle.State = puzzle.parse_instructions(self.message)

        # Execute / Verify
        # ----
        puzzle.run_polymer_step(state)
        self.assertEqual(state['value'], 'NCNBCHB')
        puzzle.run_polymer_step(state)
        self.assertEqual(state['value'], 'NBCCNBBBCBHCB')
        puzzle.run_polymer_step(state)
        self.assertEqual(state['value'], 'NBBBCNCCNBBNBNBBCHBHHBCHB')
        puzzle.run_polymer_step(state)
        self.assertEqual(state['value'], 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')

    def test_compute_10_step_score(self):

        # Setup
        # ----
        state: puzzle.State = puzzle.parse_instructions(self.message)

        # Execute / Verify
        # ----
        score = puzzle.compute_10_step_score(state)
        self.assertEqual(score, 1588)
