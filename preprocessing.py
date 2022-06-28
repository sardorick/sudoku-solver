from os import pread
import cv2


def sort_contours(cnts, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)

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
    copy=img.copy()
    cells = []
    l_r_contours, _ = sort_contours(contours, method="top-to-bottom")
    for i in range(0,len(l_r_contours), 1):
        x,y,w,h = cv2.boundingRect(l_r_contours[i])
        coord = [x, y, w, h]
        # square_coords.append(coord)
        cell = img[y:y+h, x:x+w]
        cv2.imwrite(f'./cropped_squares_new/img-{i}.png', cell)
        # cells.append(cell)

        # cv2.rectangle(copy, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.rectangle(copy, (x,y), (x+w, y+h), (0,255,0), 2)
    # return l_r_contours
    return copy
 

# print(crop_squares(preprocess_image('sudoku_unsolved.png'), 'sudoku_unsolved.png'))
cv2.imwrite('preprocessed_output.png', crop_squares(preprocess_image('sudoku_unsolved.png'), 'sudoku_unsolved.png'))

# crop_squares(preprocess_image('sudoku_unsolved.png'), 'sudoku_unsolved.png')
