# !/usr/bin/env python
# -*- coding: utf-8 -*-

# https://adventofcode.com/2021/day/4

from math import sqrt
import tools

def part_1(values):
    # Split values into numbers and boards.
    numbers, boards = _split_input_values(values)

    # Create list matching the boards list where 1 represents a matching number and 0, unmatched.
    matching_numbers = []
    [matching_numbers.append([0] * len(board)) for board in boards]

    # Draw each number in turn and check if a board has won (matching row or column)
    winning_number = 0
    for number in numbers:
        _match_number(number, boards, matching_numbers) # function edits matching_numbers in-place
        winning_board = _check_for_win(matching_numbers)
        if winning_board is not None:
            winning_number = number
            break
    
    # Work out the score of the winning board and return it.
    sum = _winning_board_sum(boards[winning_board], matching_numbers[winning_board])
    return sum * winning_number

def _split_input_values(values:str) -> set[list[int], list[list[int]]]:
    numbers = [int(x) for x in values[0][:-1].split(",")] # remove \n at end and split on comma, converting to int
    values = values[2:] # remove the numbers and blank line from values

    boards = []
    cur_board = []
    for row in values:
        if row == "\n":
            boards.append(cur_board)
            cur_board = []
            continue

        bingo_row = row.replace("\n", "").split()
        [cur_board.append(int(x)) for x in bingo_row if x != " "]
    boards.append(cur_board) # append the final board

    return numbers, boards

def _match_number(number:int, boards:list[list[int]], matching_numbers:list[list[int]]):
    """checks each board in boards for the given number and if found, flips the corresponding spot on matching_numbers to 1."""
    for board_num, board in enumerate(boards):
        for element_num, value in enumerate(board):
            if value == number: 
                matching_numbers[board_num][element_num] = 1

def _check_for_win(matching_numbers:list[list]):
    """Checks for a row or column of all 1's, returns the number of the matching board if so, else returns None."""
    number_of_rows = round(sqrt(len(matching_numbers[0]))) # also number of columns. Should be 5.
    for board_number, board in enumerate(matching_numbers):
        # Check if there is a row full of 1s
        row_num = 0
        row_start = 0
        row_end = number_of_rows
        while row_num < number_of_rows:
            print("board: ", board_number, " row: ", row_num, " values: ", board[row_start:row_end])
            is_winner =_check_line(board[row_start:row_end])
            if is_winner:
                print("^WIN. Board: ", board)
                return board_number
            
            # Prepare for the next iteration
            row_num += 1
            row_start = row_end
            row_end = ((row_num + 1) * number_of_rows)
        
        # If there is no matching rows, check columns
        col_num = 0
        col_start = 0
        while col_num < number_of_rows:
            is_winner = _check_line(board[col_start::number_of_rows]) # step equal to the row length gives column
            if is_winner:
                return board_number
            
            # Prepare for the next iteration
            col_num += 1
            col_start += 1

    return None 
    
def _check_line(line:list) -> bool:
    """Returns True if every element in the given list is 1, otherwise returns False."""
    return True if line.count(1) == len(line) else False

def _winning_board_sum(board:list[int], matching_numbers:list[int]) -> int:
    """Finds the sum of all unmarked numbers (where the equivalent matching_numbers value is 0) and returns it."""
    total = 0
    for value, match in zip(board, matching_numbers):
        if match == 0: 
            total += value
    return total

def part_1_test(values):
    result = part_1(values)
    print(f"Result (should be 4512): {result}")

def part_2(values):
    # Split values into numbers and boards.
    numbers, boards = _split_input_values(values)

    # Create list matching the boards list where 1 represents a matching number and 0, unmatched.
    matching_numbers = []
    [matching_numbers.append([0] * len(board)) for board in boards]

    # Draw each number in turn and check if a board has won (matching row or column). When it wins, remove it from the set of boards until none remain - the last board to be removed is the winner.
    winning_number = 0
    for number in numbers:
        _match_number(number, boards, matching_numbers) # function edits matching_numbers in-place
        is_final_winner = _remove_all_winning_boards(boards, matching_numbers) # function will pop winners from given parameters
        if is_final_winner:
            winning_number = number
            break
    
    # Work out the score of the winning board (which should be the only one remaining) and return it.
    sum = _winning_board_sum(boards[0], matching_numbers[0])
    return sum * winning_number

def _remove_all_winning_boards(boards:list[list[int]], matching_numbers:list[list[int]]) -> bool:
    """Removes all winning boards from boards and matching_numbers. Returns True if the winning board is the last one remaining, otherwise returns False (once all boards are removed)."""
    winning_board = _check_for_win(matching_numbers)
    if winning_board is None:
        return False
    if winning_board == 0 and len(boards) == 1:
        return True
    
    boards.pop(winning_board)
    matching_numbers.pop(winning_board)
    result = _remove_all_winning_boards(boards, matching_numbers)
    return result

def part_2_test(values):
    result = part_2(values)
    print(f"Result (should be 1924): {result}")


if __name__ == "__main__":
    test_values = ["7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n",\
"\n",\
"22 13 17 11  0\n",\
" 8  2 23  4 24\n",\
"21  9 14 16  7\n",\
" 6 10  3 18  5\n",\
" 1 12 20 15 19\n",\
"\n",\
" 3 15  0  2 22\n",\
" 9 18 13 17  5\n",\
"19  8  7 25 23\n",\
"20 11 10 24  4\n",\
"14 21 16 12  6\n",\
"\n",\
"14 21 17 24  4\n",\
"10 16 15  9 19\n",\
"18  8 23 26 20\n",\
"22 11 13  6  5\n",\
" 2  0 12  3  7\n"]
    # part_1_test(test_values)
    part_2_test(test_values)

    values = tools.read_data("4.txt")

    p1 = part_1(values)
    print(f"Part 1: {p1}")

    p2 = part_2(values)
    print(f"Part 2: {p2}")