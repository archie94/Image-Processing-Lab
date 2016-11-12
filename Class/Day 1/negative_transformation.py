# Basic Gray level transformations: Negative Transformation

import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('../../Image/low_contrast.jpg', 0)

img2 = img

img2 = 255 - img2

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img2, cmap='gray'), plt.title('Negative transformation')
plt.xticks([]), plt.yticks([])
plt.show()

"""
cv2.imshow('out', img)
cv2.waitKey(0)
"""