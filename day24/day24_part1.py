from typing import Dict, FrozenSet, List, Callable, NewType, Optional, Set, Tuple, TypedDict
import copy
import re

class Instruction(TypedDict):
    name: str
    arg_a: str
    arg_b: Optional[str]

class InvalidInputs(Exception):
    pass

def do_inp(inputs: List[int], vars: Dict[str,int], arg_a: str, arg_b: Optional[str]) -> None:
    vars[arg_a] = int(inputs.pop(0))

def do_add(inputs: List[int], vars: Dict[str,int], arg_a: str, arg_b: Optional[str]) -> None:
    assert arg_b is not None
    value: int
    if is_number(arg_b):
        value = int(arg_b)
    else:
        vars.setdefault(arg_b, 0)
        value = vars[arg_b]
    vars.setdefault(arg_a, 0)
    vars[arg_a] += value

def do_mul(inputs: List[int], vars: Dict[str,int], arg_a: str, arg_b: Optional[str]) -> None:
    assert arg_b is not None
    value: int
    if is_number(arg_b):
        value = int(arg_b)
    else:
        vars.setdefault(arg_b, 0)
        value = vars[arg_b]
    vars.setdefault(arg_a, 0)
    vars[arg_a] *= value

def do_div(inputs: List[int], vars: Dict[str,int], arg_a: str, arg_b: Optional[str]) -> None:
    assert arg_b is not None
    value: int
    if is_number(arg_b):
        value = int(arg_b)
    else:
        vars.setdefault(arg_b, 0)
        value = vars[arg_b]
    vars.setdefault(arg_a, 0)
    vars[arg_a] = int(vars[arg_a] / value)

def do_mod(inputs: List[int], vars: Dict[str,int], arg_a: str, arg_b: Optional[str]) -> None:
    assert arg_b is not None
    value: int
    if is_number(arg_b):
        value = int(arg_b)
    else:
        vars.setdefault(arg_b, 0)
        value = vars[arg_b]
    vars.setdefault(arg_a, 0)
    vars[arg_a] %= value

def do_eql(inputs: List[int], vars: Dict[str,int], arg_a: str, arg_b: Optional[str]) -> None:
    assert arg_b is not None
    value: int
    if is_number(arg_b):
        value = int(arg_b)
    else:
        value = vars[arg_b]
    vars.setdefault(arg_a, 0)
    if (vars[arg_a] == value):
        vars[arg_a] = 1
    else:
        vars[arg_a] = 0

NUMBER_PATTERN = re.compile('^-?[0-9]$')

def is_number(s: str) -> bool:
    return bool(NUMBER_PATTERN.match(s))

def parse_input(message: str) -> List[Instruction]:
    instructions: List[Instruction] = []
    lines: List[str] = message.splitlines()
    line: str
    for line in lines:
        parts: List[str] = line.split(' ')
        arg_b: Optional[str] = None
        if len(parts) > 2:
            arg_b = parts[2]
        instructions.append(Instruction({
            'name': parts[0],
            'arg_a': parts[1],
            'arg_b': arg_b,
        }))
    return instructions

def execute(instructions: List[Instruction], serial_number: str) -> Dict[str,int]:

    serial_numbers: List[int] = list(map(lambda x : int(x), list(serial_number)))
    variables: Dict[str,int] = {}

    for instruction in instructions:
        name: str = instruction['name']
        action: Callable[[List[int], Dict[str,int], str, Optional[str]],None]
        if name == 'inp':
            action = do_inp
        elif name == 'add':
            action = do_add
        elif name == 'mul':
            action = do_mul
        elif name == 'div':
            action = do_div
        elif name == 'mod':
            action = do_mod
        elif name == 'eql':
            action = do_eql
        action(serial_numbers, variables, instruction['arg_a'], instruction['arg_b'])

        # TODO: Remove debug
        # print('Step: %s' % instruction)
        # print(variables)

    return variables

def find_largest_valid_serial(instructions: List[Instruction]) -> str:
    serial_number: str = '999999999999999'
    significant_digits: int = count_inp_instructions(instructions)
    while True:

        # TODO: Remove debug
        print('SERIAL: %s' % serial_number)

        variables: Dict[str,int]
        try:
            variables = execute(instructions, serial_number)
            if variables['z'] == 0:
                return serial_number
        except ZeroDivisionError:
            pass

        serial_number = get_next_serial(serial_number, significant_digits)

def contains_zero_digit(serial: int) -> bool:
    for digit in list(str(serial)):
        if digit == '0':
            return True
    return False

def get_next_serial(serial: str, significant_digits: int) -> str:
    serial_number = int(serial[0:significant_digits]) - 1

    while (contains_zero_digit(serial_number)):
        serial_number -= 1
    return str(serial_number) + serial[significant_digits:]

def count_inp_instructions(instructions: List[Instruction]) -> int:
    count: int = 0
    for instruction in instructions:
        if instruction['name'] == 'inp':
            count += 1
    return count