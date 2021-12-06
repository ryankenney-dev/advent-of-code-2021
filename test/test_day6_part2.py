import day6.day6_part2 as puzzle
from typing import List
import unittest

class TestDay5Part1(unittest.TestCase):

    message: str ='3,4,3,1,2'

    def test_parse_fish_times(self):

        # Setup
        # ----
        expected_time_counts: puzzle.CountPerTime = {
            1: 1,
            2: 1,
            3: 2,
            4: 1,
        }

        # Execute
        # ----
        time_counts: puzzle.CountPerTime = puzzle.parse_fish_times(self.message)

        # Verify
        # ----
        self.assertEqual(time_counts, expected_time_counts)

    def test_elapse_day(self):

        # Setup
        # ----
        time_counts: puzzle.CountPerTime = puzzle.parse_fish_times(self.message)
        expected_time_counts = {
            1: {
                0: 1,
                1: 1,
                2: 2,
                3: 1,
            },
            15: {
                0: 3,
                1: 5,
                2: 3,
                3: 2,
                4: 2,
                5: 1,
                6: 4,
                7: 1,
                8: 4
            }
        }

        # Execute and Verify
        # ----
        for x in range(1,15):
            time_counts = puzzle.elapse_day(time_counts)
            if x in expected_time_counts.keys():
                self.assertEqual(time_counts, expected_time_counts[x])

    def test_elapse_days_and_get_total_count(self):

        # Setup
        # ----
        time_counts: puzzle.CountPerTime = puzzle.parse_fish_times(self.message)

        # Execute and Verify
        # ----
        total_count = puzzle.elapse_days_and_get_total_count(time_counts, 256)
        self.assertEqual(total_count, 26984457539)
