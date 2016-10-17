# Basic Gray level transformations: Power Law Transformation

import numpy as np 
import cv2
from matplotlib import pyplot as plt 
import math
import copy

img = cv2.imread('../../Image/11.jpg', 0)

out_img = copy.copy(img)

# Power Law Transformation : s = c * r ^ y
# y = 1 / G, where G is gamma value
# G < 1 will shift the image towards the darker end of the spectrum
# G > 1 will make the image appear lighter
# A gamma value of G=1 will have no affect on the input image
c = 1
y = 0.5
for i in range(0, out_img.shape[0]):
	for j in range(0, out_img.shape[1]):
		out_img[i,j] = c * pow(img[i,j], y)

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(out_img, cmap='gray'), plt.title('Power Law transformation')
plt.xticks([]), plt.yticks([])
plt.show()
