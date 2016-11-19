import cv2
import numpy as np 
from matplotlib import pyplot as plt 
import math
import copy

img = cv2.imread('../Image/bike.jpg', 0)

# Scharr(<src>, <depth>, dx, dy) where dx>=0, dy>=0 and dx+dy==1
grad_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
grad_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)

abs_grad_x = cv2.convertScaleAbs(grad_x) # converting back to uint8
abs_grad_y = cv2.convertScaleAbs(grad_y)

out_img1 = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

kernel_x = np.array( [ [3,10,3], [0,0,0], [-3,-10,-3] ])
kernel_y = np.array( [ [3,0,-3], [10,0,-10], [3,0,-1] ])

out_img2_1 = cv2.filter2D(img, -1, kernel_x)
out_img2_2 = cv2.filter2D(img, -1, kernel_y)

out_img2 = cv2.addWeighted(out_img2_1, 0.5, out_img2_2, 0.5, 0)

plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(out_img1, cmap='gray'), plt.title('Sharpened with Scharr in-built')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(out_img2, cmap='gray'), plt.title('Sharpened with Scharr')
plt.xticks([]), plt.yticks([])
plt.show()
