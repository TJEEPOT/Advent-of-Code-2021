# !/usr/bin/env python
# -*- coding: utf-8 -*-

# https://adventofcode.com/2021

def read_data(filename:str) -> list[str]:
    """Takes the day number and returns the data from the corresponding txt file for that day as a list of strings."""
    with open(f"data/{filename}", "r") as f:
        values = f.readlines()
    return values

def read_ints(filename:str) -> list[int]:
    """Takes the day number and returns the data from the corresponding txt file for that day as a list of ints."""
    with open(f"data/{filename}", "r") as f:
        values = []
        for line in f:
            values.append(int(line))
    return values