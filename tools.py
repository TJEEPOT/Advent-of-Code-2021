# !/usr/bin/env python
# -*- coding: utf-8 -*-

# https://adventofcode.com/2021

def read_data(day:str) -> list[str]:
    """Takes the day number and returns the data from the corresponding txt file for that day as a list of strings."""
    with open(f"data/{day}.txt", "r") as f:
        values = f.readlines()
    return values

def read_ints(day:str) -> list[int]:
    """Takes the day number and returns the data from the corresponding txt file for that day as a list of ints."""
    with open(f"data/{day}.txt", "r") as f:
        values = []
        for line in f:
            values.append(int(line))
    return values