from typing import List, TypedDict

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
        entry['signal_patterns'] = parts[0].split(' ')
        entry['output_digits'] = parts[1].split(' ')
        entries.append(entry)
    return entries

def count_1_4_7_8_output_digits(entries: List[Entry]) -> int:
    segment_count_1_4_7_8: List[int] = [2, 4, 3, 7]
    count_of_1_4_7_8_output_digits: int = 0
    for entry in entries:
        for output_digit in entry['output_digits']:
            if len(output_digit) in segment_count_1_4_7_8:
                count_of_1_4_7_8_output_digits += 1
    return count_of_1_4_7_8_output_digits
