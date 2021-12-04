from typing import List
import copy

def parse_input(message: str) -> List[str]:
    return message.splitlines()

def compute_oxygen_generator_rating(numbers: List[str]):
    return compute_with_dominant_char(numbers, lambda count_0, count_1: (count_1 >= count_0))

def compute_co2_scrubber_rating(numbers: List[str]):
    return compute_with_dominant_char(numbers, lambda count_0, count_1: (count_1 < count_0))

def compute_with_dominant_char(numbers: List[str], select_char_1_func):
    numbers = copy.deepcopy(numbers)
    for i in range(0, len(numbers[0])):
        if len(numbers) < 2:
            break
        count_0: int = 0
        count_1: int = 0
        for number in numbers:
            if number[i] == '0':
                count_0 += 1
            else:
                count_1 += 1
        if select_char_1_func(count_0, count_1):
            filter_char = '1'
        else:
            filter_char = '0'
        next_numbers: List[str] = []
        for number in numbers:
            if number[i] == filter_char:
                next_numbers.append(number)
        numbers = next_numbers
    if len(numbers) > 1:
        raise Exception('Too many numbers left')
    return int(''.join(numbers[0]), 2)


