import day1.day1_part1 as day1_part1
import argparse
from typing import Any

# A version of argparse.ArgumentParser, that report errors
# with a non-zero exit code
class WrappedArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.exit(125, "%s: error: %s\n" % (self.prog, message))

def parse_args_or_exit():
    parser = WrappedArgumentParser(description='Runs advent of code solutions.')

    parser.add_argument("-p", "--puzzle", type=str, required=True,
                        help='The puzzle to run. For example "day1_part1".')
    global config
    config = parser.parse_args()

def day1_part1_main():
    with open("day1/input", 'r') as f:
        message = f.read()
    depths = day1_part1.parse_input(message)
    print("Depth Increments: %s" % day1_part1.count_depth_increments(depths))

config: Any = {}

parse_args_or_exit()

#day_funcs: Dict[str, Callable[[str], None]] = {
day_funcs = {
    "day1_part1": day1_part1_main 
}

day_funcs[config.puzzle]()
