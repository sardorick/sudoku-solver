import numpy as np
import cv2

def split_boxes(board):
"""split sudoku board into 81 cells."""
    rows = np.vsplit(board,9) # split image vertically
    boxes = []
    for r in rows:
        cols = np.hsplit(r,9) # split image vertically
    for box in cols:
        box = cv2.resize(box, (input_size, input_size))/255.0
        cv2.imshow("Splitted block", box)
        cv2.waitKey(50)
        boxes.append(box)
    return boxes
gray_img = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
rois = split_boxes(gray_img)
rois = np.array(rois).reshape(-1, input_size, input_size, 1)

def displayNumbers(img, numbers, color=(0, 255, 0)):
    W = int(img.shape[1]/9)
    H = int(img.shape[0]/9)
    for i in range (9):
        for j in range (9):
            if numbers[(j*9)+i] !=0:
                cv2.putText(img, str(numbers[(j*9)+i]),
                (i*W+int(W/2)-int((W/4)),int((j+0.7)*H)),
                cv2.FONT_HERSHEY_COMPLEX, 2, color,
                2, cv2.LINE_AA)
#             return img