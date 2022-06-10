
import numpy as np
import cv2

# def split_boxes(board):
# """split sudoku board into 81 cells."""
#     rows = np.vsplit(board,9) # split image vertically
#     boxes = []
#     for r in rows:
#         cols = np.hsplit(r,9) # split image vertically
#     for box in cols:
#         box = cv2.resize(box, (input_size, input_size))/255.0
#         cv2.imshow("Splitted block", box)
#         cv2.waitKey(50)
#         boxes.append(box)
#     return boxes
# gray_img = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
# rois = split_boxes(gray_img)
# rois = np.array(rois).reshape(-1, input_size, input_size, 1)

# def displayNumbers(img, numbers, color=(0, 255, 0)):
#     W = int(img.shape[1]/9)
#     H = int(img.shape[0]/9)
#     for i in range (9):
#         for j in range (9):
#             if numbers[(j*9)+i] !=0:
#                 cv2.putText(img, str(numbers[(j*9)+i]),
#                 (i*W+int(W/2)-int((W/4)),int((j+0.7)*H)),
#                 cv2.FONT_HERSHEY_COMPLEX, 2, color,
#                 2, cv2.LINE_AA)
#             return img




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