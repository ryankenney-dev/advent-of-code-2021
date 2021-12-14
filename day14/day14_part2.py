from typing import Dict, FrozenSet, List, Callable, NewType, Optional, Set, Tuple, TypedDict
import re
import sys

class State(TypedDict):
    pair_counts: Dict[str,int]
    char_counts: Dict[str,int]
    rules: List[Tuple[str,str]]

def parse_instructions(message: str) -> State:
    lines = message.splitlines()
    value = lines.pop(0)
    pair_counts: Dict[str,int] = {}
    char_counts: Dict[str,int] = {}
    for i in range(0, len(value)):
        c = value[i]
        char_counts.setdefault(c, 0)
        char_counts[c] += 1
    for i in range(0, len(value)-1):
        pair = value[i:i+2]
        pair_counts.setdefault(pair, 0)
        pair_counts[pair] += 1
    lines.pop(0)
    rules: List[Tuple[str,str]] = []
    for line in lines:
        parts = line.split(' -> ')
        rules.append((parts[0], parts[1]))
    return {
        'char_counts': char_counts,
        'pair_counts': pair_counts,
        'rules': rules
    }

def run_polymer_step(state: State):
    insertions: Dict[int,str] = {}
    pair_count_increments: Dict[str,int] = {}

    # Compute all of the changes in element pair counts
    rule_pair: str; rule_char: str;
    for (rule_pair, rule_char) in state['rules']:
        state['pair_counts'].setdefault(rule_pair, 0)
        rule_match_count: int = state['pair_counts'][rule_pair]
        left_pair: str = rule_pair[0:1] + rule_char
        right_pair: str = rule_char + rule_pair[1:2]
        
        # Increment counts of the two pairs created by slicing the rule_pair
        pair_count_increments.setdefault(left_pair, 0)
        pair_count_increments[left_pair] += rule_match_count
        pair_count_increments.setdefault(right_pair, 0)
        pair_count_increments[right_pair] += rule_match_count

        # Decrement counts of the rule_pair (which was just sliced)
        pair_count_increments.setdefault(rule_pair, 0)
        pair_count_increments[rule_pair] -= rule_match_count

        # Increment the count of chars by the number of chars added
        state['char_counts'].setdefault(rule_char, 0)
        state['char_counts'][rule_char] += rule_match_count

    # Apply all changes to element pair counts
    pair: str; incremented_value: int;
    for pair,incremented_value in pair_count_increments.items():
        state['pair_counts'][pair] += incremented_value


def compute_n_step_score(state: State, steps: int):
    for i in range(0, steps):
        run_polymer_step(state)
    max_count: int = 0
    min_count: int = sys.maxsize
    for element_count in state['char_counts'].values():
        max_count = max(element_count, max_count)
        min_count = min(element_count, min_count)
    return max_count - min_count
