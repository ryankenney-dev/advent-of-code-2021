import day14.day14_part2 as puzzle
from typing import Dict, List, Optional, Set, Tuple
import unittest

class TestDay14Part2(unittest.TestCase):

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
        expected_polymer_rounds = [
            'NNCB',
            'NCNBCHB',
            'NBCCNBBBCBHCB',
            'NBBBCNCCNBBNBNBBCHBHHBCHB',
            'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB',
        ]
        expected_char_counts: List[Dict[str, int]] = [
            {
                'N': expected_polymer_rounds[0].count('N'),
                'C': expected_polymer_rounds[0].count('C'),
                'B': expected_polymer_rounds[0].count('B'),
            },{
                'N': expected_polymer_rounds[1].count('N'),
                'C': expected_polymer_rounds[1].count('C'),
                'B': expected_polymer_rounds[1].count('B'),
                'H': expected_polymer_rounds[1].count('H'),
            },{
                'N': expected_polymer_rounds[2].count('N'),
                'C': expected_polymer_rounds[2].count('C'),
                'B': expected_polymer_rounds[2].count('B'),
                'H': expected_polymer_rounds[2].count('H'),
            },{
                'N': expected_polymer_rounds[3].count('N'),
                'C': expected_polymer_rounds[3].count('C'),
                'B': expected_polymer_rounds[3].count('B'),
                'H': expected_polymer_rounds[3].count('H'),
            },{
                'N': expected_polymer_rounds[4].count('N'),
                'C': expected_polymer_rounds[4].count('C'),
                'B': expected_polymer_rounds[4].count('B'),
                'H': expected_polymer_rounds[4].count('H'),
            }
        ]

        # Execute / Verify
        # ----

        self.assertEqual(state['char_counts'], expected_char_counts.pop(0))
        puzzle.run_polymer_step(state)
        self.assertEqual(state['char_counts'], expected_char_counts.pop(0))
        puzzle.run_polymer_step(state)
        self.assertEqual(state['char_counts'], expected_char_counts.pop(0))
        puzzle.run_polymer_step(state)
        self.assertEqual(state['char_counts'], expected_char_counts.pop(0))
        puzzle.run_polymer_step(state)
        self.assertEqual(state['char_counts'], expected_char_counts.pop(0))

    def test_compute_n_step_score(self):

        # Setup
        # ----
        state: puzzle.State = puzzle.parse_instructions(self.message)

        # Execute / Verify
        # ----
        score = puzzle.compute_n_step_score(state, 10)
        self.assertEqual(score, 1588)
        score = puzzle.compute_n_step_score(state, 30)
        self.assertEqual(score, 2188189693529)
