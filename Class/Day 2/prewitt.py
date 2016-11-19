# Sharpening filter operations - Prewitt

import cv2
import math
import copy
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('../../Image/bike.jpg', 0)

kernel_x = np.array( [ [-1,0,1], [-1,0,1], [-1,0,1] ] )
kernel_y = np.array( [ [-1,-1,-1], [0,0,0], [1,1,1] ] )

out_img = cv2.filter2D(img, -1, kernel_x)
out_img2 = cv2.filter2D(out_img, -1, kernel_y)

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(out_img2, cmap='gray'), plt.title('Sharpened with Prewitt')
plt.xticks([]), plt.yticks([])
plt.show()
