import day8.day8_part2 as puzzle
from typing import List
import unittest

class TestDay8Part1(unittest.TestCase):

    message: str ='''acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''

    def test_sorted_string(self):

        self.assertEqual(puzzle.sort_string("bdefac"), "abcdef")

    def test_parse_entries(self):

        # Setup
        # ----
        expected_entries: List[puzzle.Entry] = [{
            'signal_patterns': ['abcdefg', 'bcdef', 'acdfg', 'abcdf', 'abd', 'abcdef', 'bcdefg', 'abef', 'abcdeg', 'ab'], 'output_digits': ['bcdef', 'abcdf', 'bcdef', 'abcdf'],
        },{
            'signal_patterns': ['be', 'abcdefg', 'bcdefg', 'acdefg', 'bceg', 'cdefg', 'abdefg', 'bcdef', 'abcdf', 'bde'], 'output_digits': ['abcdefg', 'bcdef', 'bcdefg', 'bceg'],
        },{
            'signal_patterns': ['abdefg', 'bcdeg', 'bcg', 'cg', 'abcdefg', 'bdefg', 'abcdfg', 'abcde', 'bcdefg', 'cefg'], 'output_digits': ['bcdefg', 'bcg', 'abcdefg', 'cg'],
        },{
            'signal_patterns': ['abdefg', 'cg', 'abcde', 'abdfg', 'abcdfg', 'bcdefg', 'abcdg', 'acfg', 'bcg', 'abcdefg'], 'output_digits': ['cg', 'cg', 'abcdfg', 'bcg'],
        },{
            'signal_patterns': ['bcdefg', 'bcd', 'abcdef', 'abdeg', 'abcf', 'bc', 'acdef', 'abcde', 'acdefg', 'abcdefg'], 'output_digits': ['abcdef', 'abcde', 'acdefg', 'bc'],
        },{
            'signal_patterns': ['abcdefg', 'bfg', 'fg', 'abefg', 'abdef', 'cefg', 'abceg', 'abcefg', 'abcdeg', 'abcdfg'], 'output_digits': ['cefg', 'abcdefg', 'bfg', 'abefg'],
        },{
            'signal_patterns': ['abefg', 'ac', 'abcefg', 'abcdefg', 'acdefg', 'bcdfg', 'abce', 'abdefg', 'abcfg', 'acf'], 'output_digits': ['abcdefg', 'abce', 'ac', 'abcdefg'],
        },{
            'signal_patterns': ['bcdfg', 'dfg', 'abcdefg', 'cefg', 'abdefg', 'abcdef', 'bcdef', 'abcdg', 'bcdefg', 'fg'], 'output_digits': ['cefg', 'bcdef', 'cefg', 'abcdefg'],
        },{
            'signal_patterns': ['bcdefg', 'abcefg', 'bcefg', 'acdefg', 'abcdg', 'de', 'bdef', 'cde', 'abcdefg', 'bcdeg'], 'output_digits': ['de', 'abcefg', 'abcdg', 'bcefg'],
        },{
            'signal_patterns': ['abdefg', 'bcdefg', 'cdeg', 'abcef', 'bcg', 'abcdefg', 'cg', 'abcdfg', 'bdefg', 'bcefg'], 'output_digits': ['abcdefg', 'bcg', 'cg', 'bcg'],
        },{
            'signal_patterns': ['abcfg', 'cfg', 'abcdefg', 'abceg', 'fg', 'abcdeg', 'aefg', 'abcefg', 'abcdf', 'bcdefg'], 'output_digits': ['aefg', 'abcfg', 'fg', 'abceg'],
        }]

        # Execute
        # ----
        entries: List[puzzle.Entry] = puzzle.parse_entries(self.message)

        # Verify
        # ----
        self.assertEqual(entries, expected_entries)

    def test_compute_signal_digit_mapping(self):

        # Setup
        # ----
        entry: puzzle.Entry = {
            'signal_patterns': ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'], 'output_digits': ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'],
        }
        expected_mapping = {
            8: set(list('acedgfb')),
            5: set(list('cdfbe')),
            2: set(list('gcdfa')),
            3: set(list('fbcad')),
            7: set(list('dab')),
            9: set(list('cefabd')),
            6: set(list('cdfgeb')),
            4: set(list('eafb')),
            0: set(list('cagedb')),
            1: set(list('ab')),
        }

        # Execute
        # ----
        mapping = puzzle.compute_signal_digit_mapping(entry)

        # Verify
        # ----
        self.assertEqual(mapping, expected_mapping)

    def test_compute_compute_output_value(self):

        # Setup
        # ----
        entries: List[puzzle.Entry] = puzzle.parse_entries(self.message)
        expected_output_values: List[int] = [
            5353, 8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315
        ]

        # Execute / Verify
        # ----
        for i in range(0, len(entries)):
            self.assertEqual(puzzle.compute_output_value(entries[i]), expected_output_values[i])

    def test_compute_sum_of_output_values(self):

        # Setup
        # ----
        entries: List[puzzle.Entry] = puzzle.parse_entries(self.message)
        expected_output_values: List[int] = [
            5353, 8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315
        ]

        # Execute / Verify
        # ----
        self.assertEqual(puzzle.compute_sum_of_output_values(entries), sum(expected_output_values))
