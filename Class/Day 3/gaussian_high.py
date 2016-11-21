# Gaussian low pass filter 

import matplotlib.pyplot as plt 
import cv2
import copy
import math
import numpy as np 

img = cv2.imread('../../Image/do_mean.png', 0)

g_low = cv2.GaussianBlur(img, (3,3), 0)

g_high = img - g_low

plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(g_low, cmap='gray'), plt.title('G_low')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(g_high, cmap='gray'), plt.title('G_low')
plt.xticks([]), plt.yticks([])
plt.show()