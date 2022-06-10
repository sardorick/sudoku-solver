from email import header
from multiprocessing.pool import IMapIterator
import numpy as np
import pandas as pd
import base64
from PIL import Image
import io

# convert the array to a pictue of sudoku

example = np.array([[1, 7, 8, 9, 4, 6, 5, 2, 3], 
[9, 4, 3, 8, 2, 5, 7, 1, 6], 
[6, 2, 5, 1, 3, 7, 9, 4, 8], 
[4, 5, 9, 6, 1, 3, 8, 7, 2], 
[8, 6, 1, 2, 7, 4, 3, 9, 5], 
[2, 3, 7, 5, 9, 8, 4, 6, 1], 
[5, 1, 6, 4, 8, 9, 2, 3, 7], 
[7, 8, 4, 3, 6, 2, 1, 5, 9], 
[3, 9, 2, 7, 5, 1, 6, 8, 4]])


def arr_img(grid):
    # conver array to str
    grid_str = grid.astype(str)
    # define border marker with -
    row_sep = '-'*25

    # loop through rows
    for i in range(9):
        if i % 3 == 0:
            print(row_sep)
        
        row = grid_str[i]
        # print 3x3 cells with border markers
        print('| ' + ' '.join(row[0:3]) + ' | ' + ' '.join(row[3:6]) +  ' | ' + ' '.join(row[6:]) + ' |')
     
        
    print(row_sep)
    

arr_img(example)

# print(result)
# print(type(result))
# with open('img_put.txt', 'w') as f:
#     f.write(arr_img(example))

# print(example)
