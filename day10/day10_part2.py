from typing import Dict, List, Callable, NewType, Optional, Set, Tuple, TypedDict
import statistics

OPEN_CLOSE_CHARS: Dict[str,str] = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

SCORE_CHARS: Dict[str,int] = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def parse_lines(message: str) -> List[str]:
    return message.splitlines()

def get_completion_score(line: str) -> Optional[int]:
    context_stack: List[str] = []
    for c in list(line):
        if c in OPEN_CLOSE_CHARS.keys():
            context_stack.append(c)
            continue
        if c in OPEN_CLOSE_CHARS.values():
            expected_close_char = OPEN_CLOSE_CHARS[context_stack[-1]]
            if expected_close_char != c:
                # Mismatched closing char
                return None
            if len(context_stack) < 1:
                # Too many closing chars
                return None
            context_stack.pop()
    closing_chars: List[str] = []
    while len(context_stack) > 0:
        closing_chars.append(OPEN_CLOSE_CHARS[context_stack.pop()])
    score = 0
    for c in closing_chars:
        score *= 5
        score += SCORE_CHARS[c]

    return score

def get_median_completion_score(lines: List[str]) -> int:
    scores: List[int] = []
    for line in lines:
        score = get_completion_score(line)
        if score is not None:
            scores.append(score)
    return int(statistics.median(scores))