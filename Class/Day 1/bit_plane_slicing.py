# Bit Plane Slicing

import math
import cv2
import copy
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('../../Image/lena.jpg', 0)

bit_plane_8 = copy.copy(img)
bit_plane_5 = copy.copy(img)
bit_plane_4 = copy.copy(img)
bit_plane_1 = copy.copy(img)

for i in range(0, img.shape[0]):
	for j in range(0, img.shape[1]):
		bit_plane_1[i,j] = img[i,j] & 1
		bit_plane_4[i,j] = img[i,j] & 8
		bit_plane_5[i,j] = img[i,j] & 16
		bit_plane_8[i,j] = img[i,j] & 128

plt.subplot(151), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(152), plt.imshow(bit_plane_1, cmap='gray'), plt.title('Bit Plane 1')
plt.xticks([]), plt.yticks([])
plt.subplot(153), plt.imshow(bit_plane_4, cmap='gray'), plt.title('Bit Plane 4')
plt.xticks([]), plt.yticks([])
plt.subplot(154), plt.imshow(bit_plane_5, cmap='gray'), plt.title('Bit Plane 5')
plt.xticks([]), plt.yticks([])
plt.subplot(155), plt.imshow(bit_plane_8, cmap='gray'), plt.title('Bit Plane 8')
plt.xticks([]), plt.yticks([])
plt.show()
