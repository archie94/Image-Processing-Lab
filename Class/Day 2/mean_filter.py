# Order Statistic filter - mean filter

import cv2
import numpy as np 
import copy
import math
from matplotlib import pyplot as plt 

img = cv2.imread('../../Image/do_mean.png', 0)

out_img = cv2.blur(img, (5,5)) # going with 5*5 kernel size

plt.subplot(121),plt.imshow(img, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(out_img, cmap='gray'),plt.title('Blurred/Smoothened')
plt.xticks([]), plt.yticks([])
plt.show()