# Sharpening filter operations - Laplacian

import cv2
import copy
import numpy as np 
import math
from matplotlib import pyplot as plt 

img = cv2.imread('../../Image/moon.jpg', 0)

kernel = np.array( [ [0,-1,0], [-1,4,-1], [0,-1,0] ])

out_img = cv2.filter2D(img, -1, kernel)
out_img2 = cv2.Laplacian(img, cv2.CV_64F)

plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(out_img, cmap='gray'), plt.title('Sharpened with Laplacian')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(out_img, cmap='gray'), plt.title('Sharpened with Laplacian')
plt.xticks([]), plt.yticks([])
plt.show()
