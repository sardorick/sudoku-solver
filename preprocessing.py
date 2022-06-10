import cv2
import numpy as np
import matplotlib.pyplot as plt



def preprocess_image(path):
    orig_img = cv2.imread(path)
    img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (9,9), 0)
    retval, img = cv2.threshold(img, 0,255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, (9,9))

    # img = cv2.bitwise_not(img,img)
    ext_contours, ext_hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print(len(ext_contours))
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    # img = cv2.bitwise_not(img,img)
    cv2.drawContours(orig_img, contours, -1, (0, 255,0) , 2)
    cv2.drawContours(orig_img, ext_contours, -1, (0, 255,0), 2)


    return orig_img



cv2.imwrite('preprocessed_output.png', preprocess_image('sudoku_unsolved.png'))





