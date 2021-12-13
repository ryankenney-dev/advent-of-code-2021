from typing import Dict, FrozenSet, List, Optional, Set, TypeVar, TypedDict

DigitSignal = FrozenSet[str]

class Entry(TypedDict):
    signal_patterns: List[str]
    output_digits: List[str]

def parse_entries(message: str) -> List[Entry]:
    entries: List[Entry] = []
    for line in message.splitlines():
        entry: Entry = {
            'signal_patterns': [],
            'output_digits': [],
        }    
        parts = line.split(' | ')
        # TODO: These should be sets, not sorted strings, but how much cleanup do I bother with?
        entry['signal_patterns'] = list(map(lambda item: sort_string(item), parts[0].split(' ')))
        entry['output_digits'] = list(map(lambda item: sort_string(item), parts[1].split(' ')))
        entries.append(entry)
    return entries

# TODO: Remove (not needed)
def sort_string(s: str) -> str:
    return ''.join(sorted(list(s)))

T = TypeVar('T')

def get_single_item(s: FrozenSet[T]) -> T:
    assert len(s) == 1
    return list(s)[0]

def compute_signal_digit_mapping(entry: Entry) -> Dict[int, DigitSignal]:

    # Index signals by length
    signals_by_length: Dict[int,FrozenSet[DigitSignal]] = {}
    for signal_pattern_str in entry['signal_patterns']:
        # We use sets so they duplicates are filtered out
        signal_pattern: DigitSignal = frozenset(signal_pattern_str)
        signals_by_length.setdefault(len(signal_pattern), frozenset())
        signals_entry: Optional[FrozenSet[DigitSignal]] = signals_by_length.get(len(signal_pattern))
        assert signals_entry is not None
        signals_by_length[len(signal_pattern)] = signals_entry.union(frozenset({ signal_pattern }))

    known_numbers: Dict[int, DigitSignal] = {}
    known_segments: Dict[str, str] = {}

    # Breadown of Digits vs Segement Counts:
    #
    # (0,6,9): 6 segments
    # (1): 2 segements
    # (2,3,5): 5 segments
    # (4): 4 segements
    # (7): 3 segments
    # (8): 7 segments

    # 1.  We know signals "1", "4", "7", "8" (by segment counts)
    known_numbers[1] = list(signals_by_length[2])[0]
    known_numbers[4] = list(signals_by_length[4])[0]
    known_numbers[7] = list(signals_by_length[3])[0]
    known_numbers[8] = list(signals_by_length[7])[0]

    # 2.  We know segment "a" is "7" - "1"
    known_segments['a'] = get_single_item(known_numbers[7] - known_numbers[1])

    # 3.  We know signal "6" is any 6-segement signal that does not fully contain "1"
    for digit_signal in signals_by_length[6]:
        if len(known_numbers[1] - digit_signal) > 0:
            known_numbers[6] = digit_signal
            break
    assert 6 in known_numbers

    # 3b. We know segment "c" is the segment of "1" missing from "6"
    known_segments['c'] = get_single_item(known_numbers[1] - known_numbers[6])

    #  3c. We know segment "f" is the other segment from "1"
    known_segments['f'] = get_single_item(known_numbers[1] - set(known_segments['c']))
    
    # 4.  We know signal "5" is any 5-segement signal that does not contain "c"
    for digit_signal in signals_by_length[5]:
        if known_segments['c'] not in digit_signal:
            known_numbers[5] = digit_signal
            break
    assert 5 in known_numbers

    # 5.  We know signal "2" is any 5-segement signal that does not contain "f"
    for digit_signal in signals_by_length[5]:
        if known_segments['f'] not in digit_signal:
            known_numbers[2] = digit_signal
            break
    assert 2 in known_numbers

    # 6.  We know signal "3" is the remaining 5-segment signal
    for digit_signal in signals_by_length[5]:
        if digit_signal != known_numbers[2] and digit_signal != known_numbers[5]:
            known_numbers[3] = digit_signal
            break
    assert 3 in known_numbers

    # 7.  We know segment "b" is "5" - "2" - "1"
    known_segments['b'] = get_single_item(known_numbers[5] - known_numbers[2] - known_numbers[1])

    # 8.  We know segment "e" is "2" - "5" - "1"
    known_segments['e'] = get_single_item(known_numbers[2] - known_numbers[5] - known_numbers[1])

    # 9.  We know signal "9" is any 6-segement signal that does not contain "e"
    for digit_signal in signals_by_length[6]:
        if known_segments['e'] in digit_signal:
            continue
        known_numbers[9] = digit_signal
        break
    assert 9 in known_numbers

    # 10. We know signal "0" is the remaining 6-segment signal
    known_numbers[0] = get_single_item( \
        signals_by_length[6].difference({ known_numbers[6] }).difference({ known_numbers[9] }))

    # Not needed
    #
    # # 11. We know segment "d" is "8" - "0"
    # known_segments['d'] = get_single_item(known_numbers[8] - known_numbers[0])
    #
    # # 12. We know segment "g" is the remaining segment
    # all_segments = {'a','b','c','d','e','f','g'}
    # known_segments['d'] = get_single_item(all_segments - set(known_segments.values()))

    return known_numbers

def compute_output_value(entry: Entry) -> int:
    signal_digit_mapping: Dict[int, DigitSignal] = compute_signal_digit_mapping(entry)
    output_value = 0
    digit_multiplier = 1
    for output_digit_segments_str in reversed(entry['output_digits']):
        output_digit_segments = set(list(output_digit_segments_str))
        for digit,segments in signal_digit_mapping.items():
            if output_digit_segments != segments:
                continue
            output_value += digit * digit_multiplier
            digit_multiplier *= 10
            break
    return output_value

def compute_sum_of_output_values(entries: List[Entry]) -> int:
    sum: int = 0
    for entry in entries:
        sum += compute_output_value(entry)
    return sum