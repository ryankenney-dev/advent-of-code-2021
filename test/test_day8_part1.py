import day8.day8_part1 as puzzle
from typing import List
import unittest

class TestDay8Part1(unittest.TestCase):

    message: str ='''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''

    def test_parse_entries(self):

        # Setup
        # ----
        expected_entries: List[puzzle.Entry] = [{
            'signal_patterns': ['be','cfbegad','cbdgef','fgaecd','cgeb','fdcge','agebfd','fecdb','fabcd','edb'],
            'output_digits': ['fdgacbe','cefdb','cefbgd','gcbe'],
        },{
            'signal_patterns': ['edbfga','begcd','cbg','gc','gcadebf','fbgde','acbgfd','abcde','gfcbed','gfec'],
            'output_digits': ['fcgedb','cgb','dgebacf','gc'],
        },{
            'signal_patterns': ['fgaebd','cg','bdaec','gdafb','agbcfd','gdcbef','bgcad','gfac','gcb','cdgabef'],
            'output_digits': ['cg','cg','fdcagb','cbg'],
        },{
            'signal_patterns': ['fbegcd','cbd','adcefb','dageb','afcb','bc','aefdc','ecdab','fgdeca','fcdbega'],
            'output_digits': ['efabcd','cedba','gadfec','cb'],
        },{
            'signal_patterns': ['aecbfdg','fbg','gf','bafeg','dbefa','fcge','gcbea','fcaegb','dgceab','fcbdga'],
            'output_digits': ['gecf','egdcabf','bgf','bfgea'],
        },{
            'signal_patterns': ['fgeab','ca','afcebg','bdacfeg','cfaedg','gcfdb','baec','bfadeg','bafgc','acf'],
            'output_digits': ['gebdcfa','ecba','ca','fadegcb'],
        },{
            'signal_patterns': ['dbcfg','fgd','bdegcaf','fgec','aegbdf','ecdfab','fbedc','dacgb','gdcebf','gf'],
            'output_digits': ['cefg','dcbef','fcge','gbcadfe'],
        },{
            'signal_patterns': ['bdfegc','cbegaf','gecbf','dfcage','bdacg','ed','bedf','ced','adcbefg','gebcd'],
            'output_digits': ['ed','bcgafe','cdgba','cbgef'],
        },{
            'signal_patterns': ['egadfb','cdbfeg','cegd','fecab','cgb','gbdefca','cg','fgcdab','egfdb','bfceg'],
            'output_digits': ['gbdfcae','bgc','cg','cgb'],
        },{
            'signal_patterns': ['gcafb','gcf','dcaebfg','ecagb','gf','abcdeg','gaef','cafbge','fdbac','fegbdc'],
            'output_digits': ['fgae','cfgab','fg','bagce'],
        }]

        # Execute
        # ----
        entries: List[puzzle.Entry] = puzzle.parse_entries(self.message)

        # Verify
        # ----
        self.assertEqual(entries, expected_entries)

    def test_count_1_4_7_8_output_digits(self):

        # Setup
        # ----
        entries: List[puzzle.Entry] = puzzle.parse_entries(self.message)

        # Execute / Verify
        # ----
        count: int = puzzle.count_1_4_7_8_output_digits(entries)
        self.assertEqual(count, 26)
