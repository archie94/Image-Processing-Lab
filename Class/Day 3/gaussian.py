# Gaussian low pass filter at radiii values of 5,15,30,80,230
# http://dsp.stackexchange.com/questions/10057/gaussian-blur-standard-deviation-radius-and-kernel-size
# http://stackoverflow.com/questions/17841098/gaussian-blur-standard-deviation-radius-and-kernel-size
# http://chemaguerra.com/gaussian-filter-radius/

import cv2
import numpy as np 
import copy
import math
from matplotlib import pyplot as plt 

img = cv2.imread('../../Image/do_mean.png', 0)

out_img1 = cv2.GaussianBlur(img, (3,3), 0)

# considering radius = 3 * sigma 
rad = 5.0
sigma = rad/3
kernel = int(2*rad + 1)
out_img2 = cv2.GaussianBlur(img, (kernel,kernel), sigma, sigma)

rad = 15.0
sigma = rad/3
kernel = int(2*rad + 1)
out_img3 = cv2.GaussianBlur(img, (kernel,kernel), sigma, sigma)

rad = 30.0
sigma = rad/3
kernel = int(2*rad + 1)
out_img4 = cv2.GaussianBlur(img, (kernel,kernel), sigma, sigma)

rad = 80.0
sigma = rad/3
kernel = int(2*rad + 1)
out_img5 = cv2.GaussianBlur(img, (kernel,kernel), sigma, sigma)

rad = 230.0
sigma = rad/3
kernel = int(2*rad + 1)
out_img6 = cv2.GaussianBlur(img, (kernel,kernel), sigma, sigma)

plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(out_img2, cmap='gray'), plt.title('G-Blur rad 5')
plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(out_img3, cmap='gray'), plt.title('G-Blur rad 15')
plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(out_img4, cmap='gray'), plt.title('G-Blur rad 30')
plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(out_img5, cmap='gray'), plt.title('G-Blur rad 80')
plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(out_img6, cmap='gray'), plt.title('G-Blur rad 230')
plt.xticks([]), plt.yticks([])
plt.show()
