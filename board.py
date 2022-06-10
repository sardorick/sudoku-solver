
import numpy as np
import cv2





######## creating matrix and filling numbers exist in the orig image #######
def sudoku_matrix(num):
    c = 0
    grid = np.empty((9, 9))
    for i in range(9):
        for j in range(9):
            grid[i][j] = int(num[c])
            
            c += 1
    grid = np.transpose(grid)
    return grid
 
######## Creating board to show the puzzle result in terminal##############
def board(arr):
    for i in range(9):
    
        if i%3==0 :
                print("+",end="")
                print("-------+"*3)
                
        for j in range(9):
            if j%3 ==0 :
                print("",end="| ")
            print(int(arr[i][j]),end=" ")
      
        print("",end="|")       
        print()
      
    print("+",end="")
    print("-------+"*3)
    return arr      
def check_col(arr,num,col):
    if  all([num != arr[i][col] for i in range(9)]):
        return True
    return False
    

def check_row(arr,num,row):
    if  all([num != arr[row][i] for i in range(9)]):
        return True
    return False


def check_cell(arr,num,row,col):
    sectopx = 3 * (row//3)
    sectopy = 3 * (col//3)
          
    for i in range(sectopx, sectopx+3):
        for j in range(sectopy, sectopy+3):
            if arr[i][j] == num:
                return True
    return False


def empty_loc(arr,l):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                l[0]=i
                l[1]=j
                return True              
    return False            