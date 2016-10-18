# Histogram Equalization

import cv2
from matplotlib import pyplot as plt 
import numpy as np 
import copy

img = cv2.imread('../../Image/10.jpg', 0)

out_img = cv2.equalizeHist(img)

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(out_img, cmap='gray'), plt.title('Histogram Equalization')
plt.xticks([]), plt.yticks([])
plt.show()
