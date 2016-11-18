# Order Statistic filter - mean filter

import cv2
import numpy as np 
import copy
import math
from matplotlib import pyplot as plt 

img = cv2.imread('../Image/do_mean.png', 0)

kernel = np.array( [ [1,1,1], [1,1,1], [1,1,1] ])
kernel = 1.0/9.0 * kernel

out_img = cv2.filter2D(img, -1, kernel)

plt.subplot(121),plt.imshow(img, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(out_img, cmap='gray'),plt.title('Blurred/Smoothened')
plt.xticks([]), plt.yticks([])
plt.show()
