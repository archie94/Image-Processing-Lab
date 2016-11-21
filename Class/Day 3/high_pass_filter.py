# HPF

import numpy as np 
import matplotlib.pyplot as plt 
import math
import copy
import cv2

img = cv2.imread('../../Image/do_mean.png', 0)

kernel = np.array([ [1,1,1], [1,1,1], [1,1,1] ])
kernel = 1.0/9.0*kernel

out_img1 = cv2.filter2D(img, -1, kernel)
out_img1 = img - out_img1

row,col = img.shape
centre_x,centre_y = row/2, col/2

img_dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
img_dft = np.fft.fftshift(img_dft)

mask = np.zeros((row,col,2), np.uint8)
mask[0:centre_x-5, 0:centre_y-5] = 1
mask[centre_x+5:row, centre_y+5:col] = 1

fshift=img_dft*mask
f_ishift = np.fft.ifftshift(fshift)
out_img2 = cv2.idft(f_ishift)
out_img2 = cv2.magnitude(out_img2[:,:,0], out_img2[:,:,1])

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(out_img1, cmap = 'gray')
plt.title('HPF 1'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(out_img2, cmap = 'gray')
plt.title('HPF 2'), plt.xticks([]), plt.yticks([])
plt.show()
