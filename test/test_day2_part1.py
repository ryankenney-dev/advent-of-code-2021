import day2.day2_part1 as puzzle
import unittest

class TestDay1Part1(unittest.TestCase):

    message: str ='''forward 5
down 5
forward 8
up 3
down 8
forward 2'''

    def test_parsing(self):

        # Setup
        # ----
        expected_commands: List[puzzle.SubCommand] = [
            puzzle.SubCommand(action='forward', value=5),
            puzzle.SubCommand(action='down', value=5),
            puzzle.SubCommand(action='forward', value=8),
            puzzle.SubCommand(action='up', value=3),
            puzzle.SubCommand(action='down', value=8),
            puzzle.SubCommand(action='forward', value=2),
        ]
        
        # Execute
        # ----
        commands: List[puzzle.SubCommand] = puzzle.parse_input(self.message)

        # Verify
        # ----
        self.assertEqual(commands, expected_commands)

    def test_position_compute(self):

        # Execute
        # ----
        commands: List[puzzle.SubCommand] = puzzle.parse_input(self.message)
        position: puzzle.Position = puzzle.compute_position(commands)

        # Verify
        # ----
        self.assertEqual(position, puzzle.Position(horizontal=15, depth=10))
