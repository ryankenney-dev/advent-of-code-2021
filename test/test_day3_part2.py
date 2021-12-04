import day3.day3_part2 as puzzle
import unittest

class TestDay3Part2(unittest.TestCase):

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
        oxygen_generator_rating: int = puzzle.compute_oxygen_generator_rating(parsed)
        co2_scrubber_rating: int = puzzle.compute_co2_scrubber_rating(parsed)

        # Verify
        # ----
        self.assertEqual(oxygen_generator_rating, 23)
        self.assertEqual(co2_scrubber_rating, 10)
