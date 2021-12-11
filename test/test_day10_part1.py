import day10.day10_part1 as puzzle
from typing import List, Set
import unittest

class TestDay10Part1(unittest.TestCase):

    message: str ='''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''

    def test_get_corrupted_lines(self):

        # Setup
        # ----
        lines: List[str] = puzzle.parse_lines(self.message)
        expected_corrupted = [
            '{([(<{}[<>[]}>{[]{[(<()>',
            '[[<[([]))<([[{}[[()]]]',
            '[{[{({}]{}}([{[{{{}}([]',
            '[<(<(<(<{}))><([]([]()',
            '<{([([[(<>()){}]>(<<{{',
        ]

        # Execute
        # ----
        corrupted = puzzle.get_corrupted_lines(lines)

        # Verify
        # ----
        self.assertEqual(corrupted, expected_corrupted)


    def test_get_corrupted_lines_score(self):

        # Setup
        # ----
        lines: List[str] = puzzle.parse_lines(self.message)

        # Execute
        # ----
        score = puzzle.get_corrupted_lines_score(lines)

        # Verify
        # ----
        self.assertEqual(score, 26397)
