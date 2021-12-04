import day3.day3_part1 as puzzle
import unittest

class TestDay3Part1(unittest.TestCase):

    message: str ='''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

    def test_parsing(self):

        # Setup
        # ----
        expected_parsed: List[str] = [
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010',
        ]
        
        # Execute
        # ----
        actual_parsed: List[str] = puzzle.parse_input(self.message)

        # Verify
        # ----
        self.assertEqual(actual_parsed, expected_parsed)

    def test_gamma_rate(self):

        # Execute
        # ----
        parsed: List[str] = puzzle.parse_input(self.message)
        gamma_rate: int = puzzle.compute_gamma_rate(parsed)

        # Verify
        # ----
        self.assertEqual(gamma_rate, 22)

    def test_epsilon_rate(self):

        # Execute
        # ----
        parsed: List[str] = puzzle.parse_input(self.message)
        epsilon_rate: int = puzzle.compute_epsilon_rate(parsed)

        # Verify
        # ----
        self.assertEqual(epsilon_rate, 9)
