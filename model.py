from torch import nn
import torch.nn.functional as F
from os import pread
import cv2
import numpy as np
import matplotlib.pyplot as plt
from torchvision import transforms
import torch
import torch.nn.functional as F
from PIL import Image


class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, 5, 1, 2)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, 5, 1, 2)
        self.fc1 = nn.Linear(1568, 128) # 32 * 7 * 7, 128
        self.fc2 = nn.Linear(128, 32)
        self.fc3 = nn.Linear(32, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(x.shape[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        x = F.log_softmax(x, dim=1)
        return x

# model = ConvNet()
# model = torch.load('trained_model_15b.pth')
# model.eval()


def predict(model, image:str):
    img = cv2.imread(image)

    kernel=cv2.getStructuringElement(cv2.MORPH_CROSS, (15,15))

    dst=cv2.dilate(img, kernel, iterations=15)
    dst=cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel)
    dst=cv2.erode(dst, kernel, iterations=5)    
    dst=cv2.resize(dst, (28,28))
    dst = Image.fromarray(dst)

    img_transformer=transforms.Compose([transforms.Grayscale(),transforms.Resize((28, 28)), 
                transforms.ToTensor(), 
                transforms.Normalize(mean=[(0.5)], std=[(0.5)])])

    input_tensor= img_transformer(dst)
    input_batch=input_tensor.unsqueeze(0)

    output=model.forward(input_batch)
    probability=F.softmax(output, dim=1)
    result = torch.argmax(probability, dim=1)
    probability = probability.cpu().data.numpy().squeeze()
    
    return result.item()