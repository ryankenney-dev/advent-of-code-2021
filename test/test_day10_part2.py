import day10.day10_part2 as puzzle
from typing import List, Optional, Set
import unittest

class TestDay10Part2(unittest.TestCase):

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

    def test_get_completion_score(self):

        # Setup
        # ----
        lines: List[str] = puzzle.parse_lines(self.message)
        expected_scores: List[Optional[str]] = [288957, 5566, None, 1480781, None, None, 995444, None, None, 294]

        # Execute
        # ----
        scores: List[Optional[int]] = []
        for line in lines:
            scores.append(puzzle.get_completion_score(line))

        # Verify
        # ----
        self.assertEqual(scores, expected_scores)

    def test_get_median_completion_score(self):

        # Setup
        # ----
        lines: List[str] = puzzle.parse_lines(self.message)
        expected_scores: List[str] = [288957, 5566, 0, 1480781, 0, 0, 995444, 0, 0, 294]

        # Execute / Verify
        # ----
        self.assertEqual(puzzle.get_median_completion_score(lines), 288957)
