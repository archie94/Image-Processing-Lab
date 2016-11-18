# Order Statistic filter - median filter

import cv2
import math
import copy
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('../../Image/do_mean.png', 0)

out_img = cv2.medianBlur(img, 3) # going with 3*3 kernel size

plt.subplot(121),plt.imshow(img, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(out_img, cmap='gray'),plt.title('Blurred/Smoothened')
plt.xticks([]), plt.yticks([])
plt.show()
