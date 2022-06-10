import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(path):
    kernel=cv2.getStructuringElement(cv2.MORPH_CROSS, (10,10))
    orig_img = cv2.imread(path)
    img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (9,9), 0)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, (9,9))

    img = cv2.bitwise_not(img,img)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print(len(contours))
    img = cv2.bitwise_not(img,img)
    # cv2.drawContours(orig_img, contours, -1, (0, 255,0) , 1)
    # cv2.drawContours(orig_img, ext_contours, -1, (0, 255,0), 2)

    sorted_contours = sorted(contours, key = cv2.contourArea, reverse=True)
    cv2.drawContours(orig_img, sorted_contours[1:82], -1, (0, 255,0) , 1)

    # return orig_img
    return sorted_contours[1:82]


def crop_squares(contours, path):
    img = cv2.imread(path)
    x,y,w,h = cv2.boundingRect(contours[2])
    copy=img.copy()
    cv2.rectangle(copy, (x,y), (x+w, y+h), (0,255,0), 2)
    return copy
 


cv2.imwrite('preprocessed_output.png', crop_squares(preprocess_image('sudoku_unsolved.png'), 'sudoku_unsolved.png'))





