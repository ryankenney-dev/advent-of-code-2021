from typing import Dict, List, Callable, NewType, Optional, Set, Tuple, TypedDict
import sys

OPEN_CLOSE_CHARS: Dict[str,str] = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

SCORE_CHARS: Dict[str,int] = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def parse_lines(message: str) -> List[str]:
    return message.splitlines()

def get_corrupted_char(line: str) -> Optional[str]:
    context_stack: List[str] = []
    for c in list(line):
        if c in OPEN_CLOSE_CHARS.keys():
            context_stack.append(c)
            continue
        if c in OPEN_CLOSE_CHARS.values():
            expected_close_char = OPEN_CLOSE_CHARS[context_stack[-1]]
            if expected_close_char != c:
                # Mismatched closing char
                return c
            if len(context_stack) < 1:
                # Too many closing chars
                return c
            context_stack.pop()
    return None

def get_corrupted_lines(lines: List[str]) -> List[str]:
    return list(filter(lambda l: get_corrupted_char(l) is not None, lines))

def get_corrupted_lines_score(lines: List[str]) -> int:
    corrupted_chars_optional: List[Optional[str]] = list(map(lambda l: get_corrupted_char(l), lines))
    corrupted_chars: List[str] = list(filter(None, corrupted_chars_optional))
    corrupted_char_scores: List[int] = list(map(lambda c: SCORE_CHARS[c], corrupted_chars))
    return sum(corrupted_char_scores)
