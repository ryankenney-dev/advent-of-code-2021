from typing import Any, List, NewType, Tuple, Dict, Match, Optional
import copy
import re

CountPerTime = NewType('CountPerTime', Dict[int,int])

def parse_fish_times(message: str) -> CountPerTime:
    count_per_time = CountPerTime({})
    fish_times: List[int] = list(map(lambda s: int(s), message.split(',')))
    for fish_time in fish_times:
        count_per_time.setdefault(fish_time, 0)
        count_per_time[fish_time] += 1
    return count_per_time

def elapse_day(count_per_time: CountPerTime) -> CountPerTime:
    next_count_per_time: CountPerTime = CountPerTime({})
    time_value: int
    for time_value in sorted(count_per_time.keys(), reverse=True):
        fish_count = count_per_time[time_value]
        if time_value == 0:
            # Reset these fish to 6
            next_count_per_time.setdefault(6, 0)
            next_count_per_time[6] += fish_count
            # Spawn new fish
            next_count_per_time.setdefault(8, 0)
            next_count_per_time[8] += fish_count
        else:
            next_count_per_time.setdefault(time_value-1, 0)
            next_count_per_time[time_value-1] += fish_count
    return next_count_per_time

def elapse_days_and_get_total_count(count_per_time: CountPerTime, days: int) -> int:
    for x in range(0, days):
        count_per_time = elapse_day(count_per_time)
    total_count: int = 0
    for count in count_per_time.values():
        total_count += count
    return total_count