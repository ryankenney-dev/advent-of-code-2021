from typing import List, NewType, TypedDict, Tuple
import copy

def parse_input(message: str) -> List[str]:
    return message.splitlines()

def compute_gamma_rate(numbers: List[str]) -> int:
    return compute_generic_rate(numbers, 1)

def compute_epsilon_rate(numbers: List[str]) -> int:
    return compute_generic_rate(numbers, -1)

def compute_generic_rate(numbers: List[str], comparison_multiplier: int):
    gamma_rate_binary: List[str] = []
    for i in range(0, len(numbers[0])):
        count_0: int = 0
        count_1: int = 0
        for number in numbers:
            if number[i] == '0':
                count_0 += 1
            else:
                count_1 += 1
        if count_0*comparison_multiplier > count_1*comparison_multiplier:
            gamma_rate_binary.append('0')
        else:
            gamma_rate_binary.append('1')
    return int(''.join(gamma_rate_binary), 2)
