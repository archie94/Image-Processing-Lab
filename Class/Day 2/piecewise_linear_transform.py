# Piecewise linear transform

import cv2
import math
import copy
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('../../Image/10.jpg', 0)

out_img = copy.copy(img)

for i in range(0, img.shape[0]):
	for j in range(0, img.shape[1]):
		if img[i,j] <= 110:
			out_img[i,j] = 2 * img[i,j]
		elif img[i,j] <= 200:
			out_img[i,j] = img[i,j]
		else:
			out_img[i,j] = 255

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(out_img, cmap='gray'), plt.title('Piecewise linear transformation')
plt.xticks([]), plt.yticks([])
plt.show()
