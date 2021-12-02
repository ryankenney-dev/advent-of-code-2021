import day1.day1_part1 as day1_part1
import unittest

class TestDay1Part1(unittest.TestCase):

    def test_main(self):

        # Setup
        # ----
        message: str ='''199
200
208
210
200
207
240
269
260
263'''
        expected_count: int = 7
        
        # Execute
        # ----
        depths: day1_part1.DepthsList = day1_part1.parse_input(message)

        # Verify
        # ----
        self.assertEqual(day1_part1.count_depth_increments(depths), expected_count)
