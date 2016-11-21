# LPF

import numpy as np 
import matplotlib.pyplot as plt 
import math
import copy
import cv2

img = cv2.imread('../../Image/do_mean.png', 0)

kernel = np.array([ [1,1,1], [1,1,1], [1,1,1] ])
kernel = 1.0/9.0*kernel

out_img1 = cv2.filter2D(img, -1, kernel)

row,col = img.shape
centre_x,centre_y = row/2, col/2

dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((row, col, 2), np.uint8)
mask[centre_x-5:centre_x+5, centre_y-5:centre_y+5] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(out_img1, cmap = 'gray')
plt.title('LPF 1'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
plt.title('LPF 2'), plt.xticks([]), plt.yticks([])
plt.show()
