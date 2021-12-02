import day1.day1_part1 as day1_part1
import unittest

class TestDay1Part1(unittest.TestCase):

    def test_main(self):

        test_cases = [{
            'input': '''199
200
208
210
200
207
240
269
260
263''',
            'expected_count': 7,
        }]
        
        for test_case in test_cases:
            depths = day1_part1.parse_input(test_case['input'])
            self.assertEquals(day1_part1.count_depth_increments(depths), test_case['expected_count'])
