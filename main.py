import day1.day1_part1 as d1p1
import day1.day1_part2 as d1p2
import day2.day2_part1 as d2p1
import day2.day2_part2 as d2p2
import day3.day3_part1 as d3p1
import day3.day3_part2 as d3p2
import day4.day4_part1 as d4p1
import day4.day4_part2 as d4p2
import day5.day5_part1 as d5p1
import day5.day5_part2 as d5p2
import day6.day6_part1 as d6p1
import day6.day6_part2 as d6p2
import day7.day7_part1 as d7p1
import day7.day7_part2 as d7p2
import day8.day8_part1 as d8p1
import day8.day8_part2 as d8p2
import day9.day9_part1 as d9p1
import day9.day9_part2 as d9p2
import day10.day10_part1 as d10p1
import day10.day10_part2 as d10p2
import day11.day11_part1 as d11p1
import day11.day11_part2 as d11p2
import day12.day12_part1 as d12p1
import day12.day12_part2 as d12p2
import day13.day13_part1 as d13p1
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
                        help='The puzzle to run. For example "d1p1" or "all" to run all.')
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

def d3p1_main() -> None:
    with open("day3/input", 'r') as f:
        message = f.read()
    numbers: List[str] = d3p1.parse_input(message)
    gamma_rate: int = d3p1.compute_gamma_rate(numbers)
    epsilon_rate: int = d3p1.compute_epsilon_rate(numbers)
    print("Gamma: %s, Epsilon: %s, Product: %s" % (gamma_rate, epsilon_rate, gamma_rate * epsilon_rate))

def d3p2_main() -> None:
    with open("day3/input", 'r') as f:
        message = f.read()
    numbers: List[str] = d3p2.parse_input(message)
    oxygen_generator_rating: int = d3p2.compute_oxygen_generator_rating(numbers)
    co2_scrubber_rating: int = d3p2.compute_co2_scrubber_rating(numbers)
    print("oxygen_generator_rating: %s, co2_scrubber_rating: %s, product: %s" % \
        (oxygen_generator_rating, co2_scrubber_rating, oxygen_generator_rating * co2_scrubber_rating))

def d4p1_main() -> None:
    with open("day4/input", 'r') as f:
        message = f.read()
    balls: List[int] = d4p1.parse_drawn_balls(message)
    boards: List[d4p1.Board] = d4p1.parse_boards(message)
    score: int = d4p1.find_winning_board_score(balls, boards)
    print("Score: %s" % score)

def d4p2_main() -> None:
    with open("day4/input", 'r') as f:
        message = f.read()
    balls: List[int] = d4p2.parse_drawn_balls(message)
    boards: List[d4p1.Board] = d4p2.parse_boards(message)
    score: int = d4p2.find_last_winning_board_score(balls, boards)
    print("Score: %s" % score)

def d5p1_main() -> None:
    with open("day5/input", 'r') as f:
        message = f.read()
    lines: List[d5p1.Line] = d5p1.parse_lines(message)
    lines = d5p1.filter_out_diagonal_lines(lines)
    diagram: d5p1.Diagram = d5p1.render_diagram(lines)
    danger_points: int = d5p1.count_danger_points(diagram)
    print("Danger Points: %s" % danger_points)

def d5p2_main() -> None:
    with open("day5/input", 'r') as f:
        message = f.read()
    lines: List[d5p2.Line] = d5p2.parse_lines(message)
    diagram: d5p2.Diagram = d5p2.render_diagram(lines)
    danger_points: int = d5p2.count_danger_points(diagram)
    print("Danger Points: %s" % danger_points)

def d6p1_main() -> None:
    with open("day6/input", 'r') as f:
        message = f.read()
    time_counts: d6p1.CountPerTime = d6p1.parse_fish_times(message)
    fish_count = d6p1.elapse_days_and_get_total_count(time_counts, 80)
    print("Fish Count: %s" % fish_count)

def d6p2_main() -> None:
    with open("day6/input", 'r') as f:
        message = f.read()
    time_counts: d6p2.CountPerTime = d6p2.parse_fish_times(message)
    fish_count = d6p2.elapse_days_and_get_total_count(time_counts, 256)
    print("Fish Count: %s" % fish_count)

def d7p1_main() -> None:
    with open("day7/input", 'r') as f:
        message = f.read()
    positions: d7p1.Positions = d7p1.parse_positions(message)
    cheapest_cost: int = d7p1.find_cost_cheapest_position(positions)
    print("Cheapest Cost: %s" % cheapest_cost)

def d7p2_main() -> None:
    with open("day7/input", 'r') as f:
        message = f.read()
    positions: d7p2.Positions = d7p2.parse_positions(message)
    cheapest_cost: int = d7p2.find_cost_cheapest_position(positions)
    print("Cheapest Cost: %s" % cheapest_cost)

def d8p1_main() -> None:
    with open("day8/input", 'r') as f:
        message = f.read()
    entries: List[d8p1.Entry] = d8p1.parse_entries(message)
    count: int = d8p1.count_1_4_7_8_output_digits(entries)
    print("Count of 1,3,7,8 Output Digits: %s" % count)

def d8p2_main() -> None:
    with open("day8/input", 'r') as f:
        message = f.read()
    entries: List[d8p2.Entry] = d8p2.parse_entries(message)
    sum: int = d8p2.compute_sum_of_output_values(entries)
    print("Sum of Output Values: %s" % sum)

def d9p1_main() -> None:
    with open("day9/input", 'r') as f:
        message = f.read()
    board: d9p1.Board = d9p1.parse_board(message)
    sum: int = d9p1.get_sum_of_low_point_risk(board)
    print("Sum of Low Point Risk: %s" % sum)

def d9p2_main() -> None:
    with open("day9/input", 'r') as f:
        message = f.read()
    board: d9p2.Board = d9p2.parse_board(message)
    product: int = d9p2.get_product_of_largest_basin_sizes(board)
    print("Product of Largest Basin Sizes: %s" % product)

def d10p1_main() -> None:
    with open("day10/input", 'r') as f:
        message = f.read()
    lines: List[str] = d10p1.parse_lines(message)
    score: int = d10p1.get_corrupted_lines_score(lines)
    print("Syntax Error Score: %s" % score)

def d10p2_main() -> None:
    with open("day10/input", 'r') as f:
        message = f.read()
    lines: List[str] = d10p2.parse_lines(message)
    score: int = d10p2.get_median_completion_score(lines)
    print("Median Completion Score: %s" % score)

def d11p1_main() -> None:
    with open("day11/input", 'r') as f:
        message = f.read()
    board: d11p1.Board = d11p1.parse_board(message)
    for round in range(0, 100):
        d11p1.execute_round(board)
    print("Total Flashes: %s" % board['flash_count'])

def d11p2_main() -> None:
    with open("day11/input", 'r') as f:
        message = f.read()
    board: d11p2.Board = d11p2.parse_board(message)
    d11p2.execute_rounds_until_all_flash(board)
    print("Rounds: %s" % board['rounds'])

def d12p1_main() -> None:
    with open("day12/input", 'r') as f:
        message = f.read()
    connections: Dict[str, List[str]] = d12p1.parse_connections(message)
    routes = d12p1.get_all_routes(connections)
    print("Routes: %s" % len(routes))

def d12p2_main() -> None:
    with open("day12/input", 'r') as f:
        message = f.read()
    connections: Dict[str, List[str]] = d12p2.parse_connections(message)
    routes = d12p2.get_all_routes(connections)
    print("Routes: %s" % len(routes))

def d13p1_main() -> None:
    with open("day13/input", 'r') as f:
        message = f.read()
    board: d13p1.Board = d13p1.parse_instructions(message)
    d13p1.fold_board(board)
    print("Points: %s" % len(board['points']))

def main():
    config: Any = parse_args_or_exit()
    
    day_funcs: Dict[str, Callable[[], None]] = {
        "d1p1": d1p1_main,
        "d1p2": d1p2_main,
        "d2p1": d2p1_main,
        "d2p2": d2p2_main,
        "d3p1": d3p1_main,
        "d3p2": d3p2_main,
        "d4p1": d4p1_main,
        "d4p2": d4p2_main,
        "d5p1": d5p1_main,
        "d5p2": d5p2_main,
        "d6p1": d6p1_main,
        "d6p2": d6p2_main,
        "d7p1": d7p1_main,
        "d7p2": d7p2_main,
        "d8p1": d8p1_main,
        "d8p2": d8p2_main,
        "d9p1": d9p1_main,
        "d9p2": d9p2_main,
        "d10p1": d10p1_main,
        "d10p2": d10p2_main,
        "d11p1": d11p1_main,
        "d11p2": d11p2_main,
        "d12p1": d12p1_main,
        "d12p2": d12p2_main,
        "d13p1": d13p1_main,
    }
    
    if config.puzzle == 'all':
        for k in day_funcs.keys():
            print("=== %s ===" % k)
            day_funcs[k]()
    else:
        print("=== config.puzzle ===" % k)
        day_funcs[config.puzzle]()

main()
