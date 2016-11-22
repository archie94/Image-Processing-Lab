# Suppose that a digital image is subject to histogram equalisation. Show that the second pass of histogram equalisation is same as the first pass

import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('../../Image/lena.jpg', 0)

e1 = cv2.equalizeHist(img)
e2 = cv2.equalizeHist(e1)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(e1, cmap = 'gray')
plt.title('first pass'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(e2, cmap = 'gray')
plt.title('second pass'), plt.xticks([]), plt.yticks([])
plt.show()
