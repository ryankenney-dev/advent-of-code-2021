import day12.day12_part2 as puzzle
from typing import Dict, List, Optional, Set, Tuple
import unittest

class TestDay12Part2(unittest.TestCase):

    message: str ='''start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''

    def test_parse_board(self):

        # Setup
        # ----
        expected_connections: Dict[str, List[str]] = {
            'start': ['A', 'b'],
            'A': ['start', 'c', 'b', 'end'],
            'b': ['start', 'A', 'd', 'end'],
            'c': ['A'],
            'd': ['b'],
            'end': ['A', 'b'],
        }

        # Execute
        # ----
        connections: Dict[str, List[str]] = puzzle.parse_connections(self.message)

        # Verify
        # ----
        self.assertEqual(connections, expected_connections)

    def test_is_small_cave(self):
        self.assertEqual(False, puzzle.is_small_cave('A'))
        self.assertEqual(False, puzzle.is_small_cave('Z'))
        self.assertEqual(False, puzzle.is_small_cave('AA'))
        self.assertEqual(False, puzzle.is_small_cave('ZZ'))
        self.assertEqual(True, puzzle.is_small_cave('aa'))
        self.assertEqual(True, puzzle.is_small_cave('zz'))
        self.assertEqual(False, puzzle.is_small_cave('start'))
        self.assertEqual(False, puzzle.is_small_cave('end'))

    def test_get_all_routes(self):

        # Setup
        # ----
        connections: Dict[str, List[str]] = puzzle.parse_connections(self.message)
        expected_routes: Set[Tuple[str,...]] = {
            ('start','A','b','A','b','A','c','A','end'),
            ('start','A','b','A','b','A','end'),
            ('start','A','b','A','b','end'),
            ('start','A','b','A','c','A','b','A','end'),
            ('start','A','b','A','c','A','b','end'),
            ('start','A','b','A','c','A','c','A','end'),
            ('start','A','b','A','c','A','end'),
            ('start','A','b','A','end'),
            ('start','A','b','d','b','A','c','A','end'),
            ('start','A','b','d','b','A','end'),
            ('start','A','b','d','b','end'),
            ('start','A','b','end'),
            ('start','A','c','A','b','A','b','A','end'),
            ('start','A','c','A','b','A','b','end'),
            ('start','A','c','A','b','A','c','A','end'),
            ('start','A','c','A','b','A','end'),
            ('start','A','c','A','b','d','b','A','end'),
            ('start','A','c','A','b','d','b','end'),
            ('start','A','c','A','b','end'),
            ('start','A','c','A','c','A','b','A','end'),
            ('start','A','c','A','c','A','b','end'),
            ('start','A','c','A','c','A','end'),
            ('start','A','c','A','end'),
            ('start','A','end'),
            ('start','b','A','b','A','c','A','end'),
            ('start','b','A','b','A','end'),
            ('start','b','A','b','end'),
            ('start','b','A','c','A','b','A','end'),
            ('start','b','A','c','A','b','end'),
            ('start','b','A','c','A','c','A','end'),
            ('start','b','A','c','A','end'),
            ('start','b','A','end'),
            ('start','b','d','b','A','c','A','end'),
            ('start','b','d','b','A','end'),
            ('start','b','d','b','end'),
            ('start','b','end'),
        }

        # Execute
        # ----
        routes: Set[List[str]] = puzzle.get_all_routes(connections)

        # Verify
        # ----

        print('sizes: %s %s' % (len(routes), len(expected_routes)))
        self.assertEqual(routes, expected_routes)
