# !/usr/bin/env python
# -*- coding: utf-8 -*-

# https://adventofcode.com/2021/day/2

import tools

def part_1(values):
    """Every time the request is "forward", increase the value to hor_pos by the given amount. When the request is "down", increase the value of depth by the given amount. When the request is "up", reduce the value of depth by the given amount."""
    hor_pos = 0
    depth = 0

    for value in values:
        split_val = value.split(" ")
        command = split_val[0]
        units = int(split_val[1])
        
        match command: # Python 3.10 only
            case "forward":
                hor_pos += units
            case "down":
                depth += units
            case "up":
                depth -= units
            case _:
                print("Invalid command detected: " + command[0] + "\nFull value: " + value)
                return (0, 0)

    return (hor_pos, depth)

def part_2(values):
    """The "forward" value increases the value of the hor_pos by the given amount and the value of depth by aim times the given amount. "up" decreases aim by the given amount. "down" increases aim by the given amount."""
    hor_pos = 0
    depth = 0
    aim = 0

    for value in values:
        split_val = value.split(" ")
        command = split_val[0]
        units = int(split_val[1])

        match command: # Python 3.10 only
            case "forward":
                hor_pos += units
                depth += (aim * units)
            case "down":
                aim += units
            case "up":
                aim -= units
            case _:
                print("Invalid command detected: " + command[0] + "\nFull value: " + value)
                return (0, 0)

    return (hor_pos, depth)


if __name__ == "__main__":
    values = tools.read_data("2.txt")
    hor_pos, depth = part_1(values)
    print(f"Part 1: pos = {hor_pos}, depth = {depth}. Multiplied is: {hor_pos*depth}")

    hor_pos, depth = part_2(values)
    print(f"Part 2: pos = {hor_pos}, depth = {depth}. Multiplied is: {hor_pos*depth}")