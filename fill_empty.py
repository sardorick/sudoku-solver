import cv2
import numpy as np
import matplotlib.pyplot as plt

example = [[1, 7, 8, 9, 4, 6, 5, 2, 3], 
[9, 4, 3, 8, 2, 5, 7, 1, 6], 
[6, 2, 5, 1, 3, 7, 9, 4, 8], 
[4, 5, 9, 6, 1, 3, 8, 7, 2], 
[8, 6, 1, 2, 7, 4, 3, 9, 5], 
[2, 3, 7, 5, 9, 8, 4, 6, 1], 
[5, 1, 6, 4, 8, 9, 2, 3, 7], 
[7, 8, 4, 3, 6, 2, 1, 5, 9], 
[3, 9, 2, 7, 5, 1, 6, 8, 4]]

img = cv2.imread('/Users/szokirov/Documents/GitHub/sudoku-solver/empty_board.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# plt.imshow(img_gray, cmap='gray')
# plt.show()

# for item in example:
#     for item in item:
#         print(item)

# copy = img.copy()
# for item in example:
#     for x in item:
#         x = x.astype(str)

#         for interval in range(0, 1000, 50):

#             cv2.putText(copy, x, (19+interval, 21), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
#         plt.imshow(copy)
#         plt.show()

# def split_boxes(board):
#     """split sudoku board into 81 cells."""
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
#     for i in range(9):
#         for j in range(9):
#             if numbers[(j*9)+i] !=0:
#                 cv2.putText(img, str(numbers[(j*9)+i]),
#                 (i*W+int(W/2)-int((W/4)),int((j+0.7)*H)),
#                 cv2.FONT_HERSHEY_COMPLEX, 2, color,
#                 2, cv2.LINE_AA)

# displayNumbers(img, example)