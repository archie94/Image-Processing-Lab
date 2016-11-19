# Sharpening filter - Sobel Y

import cv2
import math
import copy
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('../../Image/moon.jpg', 0)

kernel = np.array( [ [1,2,1], [0,0,0], [-1,-2,-1] ])

out_img = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(out_img, cmap='gray'), plt.title('Sharpened via Sobel Y')
plt.xticks([]), plt.yticks([])
plt.show()
