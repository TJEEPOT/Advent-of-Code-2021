# !/usr/bin/env python
# -*- coding: utf-8 -*-

# https://adventofcode.com/2021/day/6

import tools

def part_1(values):
    # Convert string input to list of population counts.
    population = _convert_values_to_population_categories(values)

    # Simulate the next 80 days of fish population growth.
    day_number = 0
    while day_number < 80:
        _simulate_one_day_growth(population)
        day_number += 1

    # Return the count of fish now in the population
    return sum(population)

def _simulate_one_day_growth(population:list[int]):
    """Takes a population distribution and simulates a day of growth (in place)."""
    birthing_fish = population[0]
    for fish_category_id in range(0, len(population)-1):
        population[fish_category_id] = population[fish_category_id+1]
    population[6] += birthing_fish # fish giving birth are added to category 6
    population[8] = birthing_fish # newly born fish added to the end of the list, overwriting the old value

def _convert_values_to_population_categories(values:str) -> list[int]:
    """Takes a string of values separated by commas and returns a list where each element is the number of fish of that "age"."""
    val_list = list(map(int, values[0].split(',')))
    fish_categories = [0] * 9 # number of fish of each "age", with new fish being pos[8]
    for fish in val_list:
        fish_categories[fish] += 1
        
    return fish_categories

def part_1_test(values):
    pop = _convert_values_to_population_categories(values)
    _simulate_one_day_growth(pop)
    print("After 1 day (expecting [1, 1, 2, 1, 0, 0, 0, 0, 0]", pop)

    _simulate_one_day_growth(pop)
    print("After 2 days (expecting [1, 2, 1, 0, 0, 0, 1, 0, 1]", pop)

    result = part_1(values)
    print(f"Part 1 test result (should be 5934): {result}")

def part_2(values):
    # Convert string input to list of ints.
    population = _convert_values_to_population_categories(values)

    # Simulate the next 256 days of fish population growth.
    day_number = 0
    while day_number < 256:
        _simulate_one_day_growth(population)
        day_number += 1

    # Return the count of fish now in the population
    return sum(population)

def part_2_test(values):
    result = part_2(values)
    print(f"Part 2 test result (should be 26984457539): {result}")


if __name__ == "__main__":
    test_values = ["3,4,3,1,2"]
    # part_1_test(test_values)
    part_2_test(test_values)

    values = tools.read_data("6.txt")

    p1 = part_1(values)
    print(f"Part 1: {p1}")

    p2 = part_2(values)
    print(f"Part 2: {p2}")