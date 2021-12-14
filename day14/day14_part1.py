from typing import Dict, FrozenSet, List, Callable, NewType, Optional, Set, Tuple, TypedDict
import re
import sys

class State(TypedDict):
    value: str
    rules: List[Tuple[str,str]]

def parse_instructions(message: str) -> State:
    lines = message.splitlines()
    value = lines.pop(0)
    lines.pop(0)
    rules: List[Tuple[str,str]] = []
    for line in lines:
        parts = line.split(' -> ')
        rules.append((parts[0], parts[1]))
    return {
        'value': value,
        'rules': rules
    }

def run_polymer_step(state: State):
    insertions: Dict[int,str] = {}
    locations: List[int]; location: int;
    rule_key: str; rule_value: str;
    for (rule_key, rule_value) in state['rules']:
        locations = find_all_match_locations(rule_key, state['value'])
        for location in locations:
            insertions[location+1] = rule_value
    new_value = list(state['value'])
    locations = sorted(list(insertions.keys()),reverse=True)
    for location in locations:
        new_value.insert(location, insertions[location])
    state['value'] = ''.join(new_value)

# NOTE: This includes overlapping matches (unlike regex)
def find_all_match_locations(pattern: str, s: str) -> List[int]:
    result: List[int] = []
    for i in range(0, len(s)):
        matches: bool = True
        for pattern_i in range(0, len(pattern)):
            if i+pattern_i >= len(s):
                matches = False
                break
            if s[i+pattern_i] != pattern[pattern_i]:
                matches = False
                break
        if matches:
            result.append(i)
    return result

def compute_10_step_score(state: State):
    for i in range(0, 10):
        run_polymer_step(state)
    element_list: List[str] = list(state['value'])
    element_set: Set[str] = set(element_list)
    max_count: int = 0
    min_count: int = sys.maxsize
    for element in element_set:
        count = state['value'].count(element)
        max_count = max(count, max_count)
        min_count = min(count, min_count)
    return max_count - min_count
