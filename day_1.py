# !/usr/bin/env python
# -*- coding: utf-8 -*-

# https://adventofcode.com/2021/day/1

import tools

def part_1(values):
    previous_measurement = values[0] # the first measurement will be read twice but that won't be an issue here.
    greater_count = 0 # count of times where the current sum is larger than the previous sum

    for measurement in values:
        if measurement > previous_measurement:
            greater_count += 1
        previous_measurement = measurement
    return greater_count
    

def part_2(values):
    """You don't need to read, store and sum every set of three values for this one. Since both sets share two values, only the first value from set 1 and the last value from set 2 need to be checked. Since the latter element is the former element+3 in the list, we don't need to store any data between checks except the total count of instances where the second value was greater than the first."""
    greater_count = 0 # count of times where the current sum is larger than the previous sum

    for i in range(0, len(values)-3): # ensure we don't check past the end of the list
        prev_val = values[i] # the first value from the previous set
        cur_val = values[i+3] # the last value from the current set
        if cur_val > prev_val:
            greater_count += 1

    return greater_count


if __name__ == "__main__":
    values = tools.read_ints("1")
    print("Part 1: " + part_1(values))
    print("Part 2: " + part_2(values))