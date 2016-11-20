# Discrete Fourier Transform
# read : http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html

import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import math
import copy

img = cv2.imread('../../Image/messi.jpg', 0)

f = np.fft.fft2(img) # numpy's fast fourier transform algo 
fshift = np.fft.fftshift(f) # bring zero frequency component to center
magnitude_spectrum_numpy = 20*np.log(np.abs(fshift))

rows, cols = img.shape
crow, ccol = rows/2, cols/2
# remove the low frequencies by masking with a rectangular window of size 60x60
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift) # this returns a complex number
img_back = np.abs(img_back)

# Now do same thing with OpenCv 
dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft) # bring zero frequency component to center
magnitude_spectrum_cv2 = 20*np.log(cv2.magnitude( dft_shift[:,:,0], dft_shift[:,:,1] ))

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back2 = cv2.idft(f_ishift)
img_back2 = cv2.magnitude(img_back2[:,:,0],img_back2[:,:,1])

plt.subplot(231),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(magnitude_spectrum_numpy, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(magnitude_spectrum_cv2, cmap = 'gray')
plt.title('Magnitude Spectrum in cv2'), plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(img_back2, cmap = 'gray')
plt.title('Image after HPF cv2'), plt.xticks([]), plt.yticks([])
plt.show()
