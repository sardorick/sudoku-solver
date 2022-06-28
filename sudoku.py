import numpy as np
import math

sud_size = 9

def is_free(grid, row, col, num):
    # check if there are similar numbers in the row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # check if we have same number in column
    for x in range(9):
        if grid[x][col] == num:
            return False
    
    # check if we have same number in the same 3x3 cell
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i+start_row][j+start_col] == num:
                return False
    return True

def sudoku(grid, row, col):
    # check if we are in the last row, we return true to avoid infinite loop
    if (row == sud_size - 1 and col == sud_size):
        return True

    # check if we are in the last column and move to next one if yes
    if col == sud_size:
        row += 1
        col = 0

    # check if current position is >0, go to next col
    if grid[row][col] > 0:
        return sudoku(grid, row, col+1)
    # check if the cell is free to place a number and move to next col
    for num in range(1, sud_size+1, 1):
        if is_free(grid, row, col, num):
            grid[row][col] = num

            # check for next iteration
            if sudoku(grid, row, col+1):
                return True

        # restart count if number is not correct
        grid[row][col] = 0

    return False

# test
# grid = [[0, 7, 8, 0, 0,6, 0, 2, 3],
#         [0, 4, 3, 0, 2, 0, 0, 0, 6],
#         [0, 0, 0, 0, 3, 7, 9, 0, 8],
#         [0, 5, 0, 0, 0, 3, 8, 0, 2],
#         [0, 6, 0, 0, 0, 0, 0, 9, 0],
#         [2, 0, 7, 5, 0, 0, 0, 6, 0],
#         [5, 0, 6, 4, 8, 0, 0, 0, 0],
#         [7, 0, 0, 0, 6, 0, 1, 5, 0],
#         [3, 9, 0, 7, 0, 0, 6, 8, 0]]

# if (sudoku(grid, 0, 0)):
#     print(grid)
# else:
#     print('no')



"""
[[1, 7, 8, 9, 4, 6, 5, 2, 3], 
[9, 4, 3, 8, 2, 5, 7, 1, 6], 
[6, 2, 5, 1, 3, 7, 9, 4, 8], 
[4, 5, 9, 6, 1, 3, 8, 7, 2], 
[8, 6, 1, 2, 7, 4, 3, 9, 5], 
[2, 3, 7, 5, 9, 8, 4, 6, 1], 
[5, 1, 6, 4, 8, 9, 2, 3, 7], 
[7, 8, 4, 3, 6, 2, 1, 5, 9], 
[3, 9, 2, 7, 5, 1, 6, 8, 4]]
"""