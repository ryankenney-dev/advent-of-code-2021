from unittest.case import expectedFailure
import day24.day24_part1 as puzzle
from typing import Dict, List, Optional, Set, Tuple
import unittest

class TestDay24Part1(unittest.TestCase):

    def test_parse_input(self):

        # Setup
        # ----
        message: str ='''inp z
inp x
mul z 3
eql z x'''
        expected_instructions: List[puzzle.Instruction] = [
            puzzle.Instruction({ 'name': 'inp', 'arg_a': 'z', 'arg_b': None }),
            puzzle.Instruction({ 'name': 'inp', 'arg_a': 'x', 'arg_b': None }),
            puzzle.Instruction({ 'name': 'mul', 'arg_a': 'z', 'arg_b': '3' }),
            puzzle.Instruction({ 'name': 'eql', 'arg_a': 'z', 'arg_b': 'x' }),
        ]

        # Execute
        # ----
        instructions: List[puzzle.Instruction] = puzzle.parse_input(message)

        # Verify
        # ----
        self.assertEqual(instructions, expected_instructions)

    def test_get_next_serial(self):

        # Execute / Verify
        # ----
        # ... With 2 significant digits
        self.assertEqual(puzzle.get_next_serial('99999999999999', 2), '98999999999999')
        # ... With 5 significant digits
        self.assertEqual(puzzle.get_next_serial('99999999999999', 5), '99998999999999')
        # ... Rolled past 0
        self.assertEqual(puzzle.get_next_serial('99991999999999', 5), '99989999999999')

    def test_count_inp_instructions(self):

        # Setup
        # ----
        message: str ='''inp z
inp x
mul z 3
eql z x
inp y'''
        instructions: List[puzzle.Instruction] = puzzle.parse_input(message)

        # Execute / Verify
        # ----
        self.assertEqual(puzzle.count_inp_instructions(instructions), 3)
