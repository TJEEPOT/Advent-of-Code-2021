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
    gamma_int = _convert_binary_str_to_int(gamma)
    epsilon_int = _convert_binary_str_to_int(epsilon)

    # Return the product of those values.
    return gamma_int * epsilon_int

def _convert_binary_str_to_int(binary_value: str) -> int:
    """Finds and returns the integer representation of a binary string."""
    binary_value = binary_value[::-1] # reverse the string to represent a little endian value
    int_value = 0
    for counter, bit in enumerate(binary_value):
        bit_value = int(bit) * (2 **counter)
        int_value += bit_value
    return int_value

def _part_1_test():
    values = ["1101011010\n", "0110101110\n", "1010101001\n"]
    test_int = _convert_binary_str_to_int("1101011010")
    print(f"Testing binary converter (should be 858): {test_int}")
    answer = part_1(values) # ("1110101010" = 938) * ("0001010101" = 85) = 79730
    print(f"Testing part 1 solver (should be 79730): {answer}")

def part_2(values):
    # Find ratings with bit criteria
    oxygen = _find_rating(values, 0, True)
    co2 = _find_rating(values, 0, False)

    # Convert to decimal
    oxygen_int = _convert_binary_str_to_int(oxygen)
    co2_int = _convert_binary_str_to_int(co2)

    # return the product
    return oxygen_int * co2_int

def _find_rating(values: list, bit_position: int, find_most_common: bool) -> str:
    """Recursively find the one value from values which fits the requirements and return it."""
    if len(values) == 1:
        return values[0][:-1] # remove the \n
    
    value_0 = []
    value_1 = []
    for value in values:
        if value[bit_position] == "0":
            value_0.append(value)
        else:
            value_1.append(value)
    
    if (find_most_common and len(value_0) > len(value_1)) or (not find_most_common and len(value_0) <= len(value_1)):
        result = _find_rating(value_0, bit_position+1, find_most_common)
    else:
        result = _find_rating(value_1, bit_position+1, find_most_common)

    return result
    
def _part_2_test():
    values = ["00100\n", "11110\n", "10110\n", "10111\n", "10101\n", "01111\n", "00111\n", "11100\n", "10000\n", "11001\n", "00010\n", "01010\n"]
    rating = part_2(values)
    print(f"Rating (should be 230): {rating}")


if __name__ == "__main__":
    # _part_1_test()
    #_part_2_test()
    values = tools.read_data("3.txt")

    p1 = part_1(values)
    print(f"Part 1: {p1}")

    p2 = part_2(values)
    print(f"Part 2: {p2}")