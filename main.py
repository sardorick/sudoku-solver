import cv2
import numpy as np
import matplotlib.pyplot as plt
from preprocessing import preprocess_image, crop_squares, predict
from model import ConvNet
from torch import nn
import torch.nn.functional as F
import torch


cv2.imwrite('preprocessed_output.png', crop_squares(preprocess_image('sudoku_unsolved.png'), 'sudoku_unsolved.png'))

model = ConvNet()
model = torch.load('trained_model_15b.pth')
model.eval()

images, labels = next(iter(testloader))
# logits = net.forward(images[1].view(1,1,28,28))
logits = model.forward(images[1].unsqueeze(0))
ps = F.softmax(logits, dim=1)
# view_classify(images[1], ps)
print(f'The given Image was classified as: {torch.argmax(ps)}')



