# !/usr/bin/env python
# -*- coding: utf-8 -*-

# https://adventofcode.com/2021/day/3

import tools

def part_1(values):
    value_counts = [] # stores the total number of zeroes and ones for each bit
    num_chars = len(values[0])
    count = 0
    while count < num_chars - 1: # remove one for the new line character
        value_counts.append([0,0]) # 0 zeroes and 0 ones to start
        count += 1

    # Find the counts for each zero and one per bit.
    for value in values:
        for index, bit in enumerate(value):
            if bit == "0":
                value_counts[index][0] += 1
            elif bit == "1":
                value_counts[index][1] += 1

    # Find the gamma (string of most common values per bit).
    gamma = ""
    for counts in value_counts:
        if counts[0] > counts[1]:
            gamma += "0"
        else:
            gamma += "1"
    
    # Find the epsilon (opposite of gamma).
    epsilon = ""
    for char in gamma:
        if char == "0":
            epsilon += "1"
        else:
            epsilon += "0"

    # Treat gamma and epsilon as binary representations of a value and convert those values to decimal.
    gamma_int = convert_binary_str_to_int(gamma)
    epsilon_int = convert_binary_str_to_int(epsilon)

    # Return the product of those values.
    return gamma_int * epsilon_int

def convert_binary_str_to_int(binary_value: str) -> int:
    """Finds and returns the integer representation of a binary string."""
    binary_value = binary_value[::-1] # reverse the string to represent a little endian value
    int_value = 0
    for counter, bit in enumerate(binary_value):
        bit_value = int(bit) * (2 **counter)
        int_value += bit_value
    return int_value

def part_1_test():
    values = ["1101011010\n", "0110101110\n", "1010101001\n"]
    test_int = convert_binary_str_to_int("1101011010")
    print(f"Testing binary converter (should be 858): {test_int}")
    answer = part_1(values) # ("1110101010" = 938) * ("0001010101" = 85) = 79730
    print(f"Testing part 1 solver (should be 79730): {answer}")

def part_2(values):
    return 0


if __name__ == "__main__":
    # part_1_test()
    values = tools.read_data("3.txt")

    p1 = part_1(values)
    print(f"Part 1: {p1}")

    p2 = part_2(values)
    print(f"Part 2: {p2}")