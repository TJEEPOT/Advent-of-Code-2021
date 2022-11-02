# !/usr/bin/env python
# -*- coding: utf-8 -*-

# https://adventofcode.com/2021/day/2

import tools

def part_1(values):
    """Every time the request is "forward", increase the value to hor_pos by the given amount. When the request is "down", increase the value of depth by the given amount. When the request is "up", reduce the value of depth by the given amount."""
    hor_pos = 0
    depth = 0

    for value in values:
        command = value.split(" ")
        match command[0]: # Python 3.10 only
            case "forward":
                hor_pos += int(command[1])
            case "down":
                depth += int(command[1])
            case "up":
                depth -= int(command[1])
            case _:
                print("Invalid command detected: " + command[0] + "\nFull value: " + value)
                return 0

    return (hor_pos, depth)

def part_2(values):
    return 0


if __name__ == "__main__":
    values = tools.read_data("2")
    hor_pos, depth = part_1(values)
    print(f"Part 1: pos = {hor_pos}, depth = {depth}. Multiplied is: {hor_pos*depth}")

    p2 = part_2(values)
    print(f"Part 2: {p2}")