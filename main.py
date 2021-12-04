import day1.day1_part1 as d1p1
import day1.day1_part2 as d1p2
import day2.day2_part1 as d2p1
import day2.day2_part2 as d2p2
import argparse
from typing import Any, Callable, Dict, List

# A version of argparse.ArgumentParser, that report errors
# with a non-zero exit code
class WrappedArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.exit(125, "%s: error: %s\n" % (self.prog, message))

def parse_args_or_exit() -> Any:
    parser = WrappedArgumentParser(description='Runs advent of code solutions.')

    parser.add_argument("-p", "--puzzle", type=str, required=True,
                        help='The puzzle to run. For example "d1p1".')
    return parser.parse_args()

def d1p1_main() -> None:
    with open("day1/input", 'r') as f:
        message = f.read()
    depths = d1p1.parse_input(message)
    print("Depth Increments: %s" % d1p1.count_depth_increments(depths))

def d1p2_main() -> None:
    with open("day1/input", 'r') as f:
        message = f.read()
    depths = d1p2.parse_input(message)
    print("Depth Increments: %s" % d1p2.count_depth_increments(depths))

def d2p1_main() -> None:
    with open("day2/input", 'r') as f:
        message = f.read()
    commands: List[d2p1.SubCommand] = d2p1.parse_input(message)
    position: d2p1.Position = d2p1.compute_position(commands)
    print("Position: %s, Product: %s" % (position, position['horizontal'] * position['depth']))

def d2p2_main() -> None:
    with open("day2/input", 'r') as f:
        message = f.read()
    commands: List[d2p2.SubCommand] = d2p2.parse_input(message)
    position: d2p2.Position = d2p2.compute_position(commands)
    print("Position: %s, Product: %s" % (position, position['horizontal'] * position['depth']))

def main():
    config: Any = parse_args_or_exit()
    
    day_funcs: Dict[str, Callable[[], None]] = {
        "d1p1": d1p1_main,
        "d1p2": d1p2_main,
        "d2p1": d2p1_main,
        "d2p2": d2p2_main,
    }
    
    day_funcs[config.puzzle]()

main()
