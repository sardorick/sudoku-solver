import cv2
import numpy as np
import matplotlib.pyplot as plt
from preprocessing import preprocess_image, crop_squares
from model import ConvNet, predict
from torch import nn
import torch.nn.functional as F
import torch

# cv2.imwrite('preprocessed_output.png', crop_squares(preprocess_image('sudoku_unsolved.png'), 'sudoku_unsolved.png'))

net = ConvNet()
net = torch.load('trained_model_15b.pth')
# net.load_state_dict(torch.load('trained_model_15b.pth'))
net.eval()


results = []

for i in range(0,81,1):
    prediction = predict(net ,f'cropped_squares/img-{i}.png')
    results.append(prediction)

print(f'{results} | {len(results)}')


