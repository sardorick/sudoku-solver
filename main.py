import cv2
import numpy as np
from preprocessing import preprocess_image, crop_squares
from model import ConvNet, predict
from sudoku import is_free, sudoku
from array_img import arr_img
import torch
import easyocr

# cv2.imwrite('preprocessed_output.png', crop_squares(preprocess_image('sudoku_unsolved.png'), 'sudoku_unsolved.png'))

net = ConvNet()
net = torch.load('trained_model_15b.pth')
# net.load_state_dict(torch.load('trained_model_15b.pth'))
net.eval()


def read_images():
    """Read images using Easy OCR and return a list of predictions"""
    results = []
    reader =  easyocr.Reader(['en'])
    for i in range(0,81,1):
        prediction = reader.readtext(f'cropped_squares/img-{i}.png')
        if prediction == []:
            results.append(0)
        for i in range(len(prediction)):
            results.append(int(prediction[i][-2]))
    return np.reshape(results, (9, 9)).T

results = read_images()
# print(results)
# if (sudoku(results, 0, 0)):
#     print(results)

if (sudoku(results, 0, 0)):
    print(results)

# def sudoku_board(x):
#     return arr_img(x)

# sudoku_board(resolved_sudoku)




