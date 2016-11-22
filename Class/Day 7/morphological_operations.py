# Dilation, Erosion, Opening, Closing, Hit or miss

import cv2
import matplotlib.pyplot as plt 
import numpy as np 
import math
import copy 

img1 = cv2.imread('../../Image/Dialation Input.JPG', 0)
img2 = cv2.imread('../../Image/Erosion2.JPG',0)
img3 = cv2.imread('../../Image/OPENING CLOSING.JPG', 0)
img4 = cv2.imread('../../Image/lena.jpg', 0)

kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(img1, kernel, iterations=1)
erosion = cv2.erode(img2, kernel, iterations=1)
opening = cv2.morphologyEx(img3, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img3, cv2.MORPH_CLOSE, kernel)

thres,im_bw = cv2.threshold(img4, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
img4 = cv2.threshold(img4, thres, 255, cv2.THRESH_BINARY)[1]
ker = np.array([[1, 0, 0], [0, 1, 1], [0, 1, 1]])
hitmiss = cv2.filter2D(img4, -1, ker)


plt.subplot(341),plt.imshow(img1, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(342),plt.imshow(dilation, cmap = 'gray')
plt.title('Dilation'), plt.xticks([]), plt.yticks([])
plt.subplot(343),plt.imshow(img2, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(344),plt.imshow(erosion, cmap = 'gray')
plt.title('Erosion'), plt.xticks([]), plt.yticks([])
plt.subplot(345),plt.imshow(img3, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(346),plt.imshow(opening, cmap = 'gray')
plt.title('Opening'), plt.xticks([]), plt.yticks([])
plt.subplot(347),plt.imshow(closing, cmap = 'gray')
plt.title('Closing'), plt.xticks([]), plt.yticks([])
plt.subplot(348),plt.imshow(img4, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(349),plt.imshow(hitmiss, cmap = 'gray')
plt.title('Hit or miss'), plt.xticks([]), plt.yticks([])

plt.show()