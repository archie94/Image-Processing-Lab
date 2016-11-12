# Basic Gray level transformations: Log Transformation

import numpy as np 
import cv2
from matplotlib import pyplot as plt 
import math
import copy

img = cv2.imread('../../Image/11.jpg', 0)

out_img = copy.copy(img)

# Log transformation : s = c * log(r + 1)
c = 5
for i in range(0, out_img.shape[0]):
	for j in range(0, out_img.shape[1]):
		out_img[i,j] = c * math.log(out_img[i,j] + 1, 2.71828)

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(out_img, cmap='gray'), plt.title('Log transformation')
plt.xticks([]), plt.yticks([])
plt.show()
