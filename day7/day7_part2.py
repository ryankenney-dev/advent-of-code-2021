from typing import Any, List, NewType, Tuple, Dict, Match, Optional
import sys
import math

Positions = NewType('Positions', List[int])

def parse_positions(message: str) -> Positions:
    return Positions(list(map(lambda x: int(x), message.split(','))))

def find_cost_cheapest_position(positions: Positions) -> int:
    min_center_position_cost: int = sys.maxsize
    min_center_position: int = sys.maxsize
    center_position: int

    position_costs: List[int] = []
    for center_position in range(min(positions), max(positions)):
        position_cost: int = 0
        for position in positions:
            delta = abs(position - center_position)
            position_cost += math.floor(delta * (delta + 1) / 2)
        position_costs.append(position_cost)
    return min(position_costs)

