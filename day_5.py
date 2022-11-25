# !/usr/bin/env python
# -*- coding: utf-8 -*-

# https://adventofcode.com/2021/day/5

import tools
import time

def part_1(values):
    # Convert the values to list of line segments
    line_segments = []
    for value in values:
        line_segments.append(_value_to_coords(value))

    # Find points between the two co-ordinates on each line segment.
    points_list = []
    for line in line_segments:
        points_on_line = _find_points_on_line(line)
        if points_on_line:
            points_list.extend(points_on_line)

    # Find how many points share the same co-ordinates.
    found_points = {}
    points_list = list(map(tuple, points_list))
    for points in points_list:
        found_points[points] = found_points.setdefault(points, 0) + 1

    # Count how many points overlap twice or more.
    overlapping_points = 0
    for number_overlapping in found_points.values():
        if number_overlapping >= 2:
            overlapping_points += 1 
       
    return overlapping_points

def _value_to_coords(value:str) -> list[list[int,int]]:
    """Takes a string from the input and converts it to a list of co-ordinates in the form [[x1,y1], [x2,y2]]."""
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    buffer = ""
    coord = []
    line_segment = []
    
    for char in value:
        if char in numbers:
            buffer = buffer + char

        elif char == ",":
            coord.append(int(buffer))
            buffer = ""
        
        elif char == "-" or char == "\n":
            coord.append(int(buffer))
            line_segment.append(coord)
            buffer = ""
            coord = []

    return line_segment
        
def _find_points_on_line(line:list[list[int,int]], horizontal=False) -> list[list[int,int]]:
    """Takes the given co-ordinates line and checks if there are points between them. Returns a list of all points co-ordinates along the given line. Horizontal setting NYI."""
    points = []
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]

    # Deal with horizontal lines (where x1 = x2).
    if x1 == x2:
        point_range = range(y1, y2+1) if y1 < y2 else range(y2, y1+1)
        [points.append([x1, y_val]) for y_val in point_range]
    
    # Deal with vertical lines (where y1 = y2).
    elif y1 == y2:
        point_range = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)
        [points.append([x_val, y1]) for x_val in point_range]
    
    # Deal with horizontal lines.
    if horizontal:
        pass

    return points

def part_1_test(values):
    test_value = _value_to_coords(values[0])
    print(f"Test value (should be [[0, 9], [5, 9]): {test_value}")

    y_forward_points = _find_points_on_line(test_value)
    print(f"Y forward test points (should be [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9]]): {x_forward_points}")

    test_value = [[2,9],[0,9]]
    y_backward_points = _find_points_on_line(test_value)
    print(f"Y backwards test (should be [[0, 9], [1, 9], [2, 9]]): {x_backward_points}")

    test_value = [[9,0],[9,2]]
    x_forward_points = _find_points_on_line(test_value)
    print(f"X forward test (should be [[9, 0], [9, 1], [9, 2]]): {y_forward_points}")

    test_value = [[9,2],[9,0]]
    x_backward_points = _find_points_on_line(test_value)
    print(f"X backward test (should be [[9, 0], [9, 1], [9, 2]]): {y_backward_points}")

    result = part_1(values)
    print(f"Part 1 Test result (should be 5): {result}")

def part_2(values):
    return 0

def part_2_test(values):
    result = part_2(values)
    print(f"Part 2 test result (should be xxx): {result}")


if __name__ == "__main__":
    test_values = ["0,9 -> 5,9\n",
"8,0 -> 0,8\n",
"9,4 -> 3,4\n",
"2,2 -> 2,1\n",
"7,0 -> 7,4\n",
"6,4 -> 2,0\n",
"0,9 -> 2,9\n",
"3,4 -> 1,4\n",
"0,0 -> 8,8\n",
"5,5 -> 8,2\n"]
    # part_1_test(test_values)
    part_2_test(test_values)

    values = tools.read_data("5.txt")

    tic = time.perf_counter()
    p1 = part_1(values)
    toc = time.perf_counter()
    time_taken = toc - tic
    print(f"Part 1: {p1}")
    print(f"Time taken (seconds): {time_taken}")

    p2 = part_2(values)
    print(f"Part 2: {p2}")