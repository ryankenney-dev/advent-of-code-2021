from typing import List
import copy

DepthsList = List[int]

def parse_input(message: str) -> DepthsList:
    return list(map(lambda x: int(x), message.splitlines()))    

def count_depth_increments(depths: DepthsList) -> int:
    depths = copy.deepcopy(depths)
    increments = 0
    while len(depths) > 1:
        previous = depths.pop(0)
        if depths[0] - previous > 0:
            increments += 1
    return increments
