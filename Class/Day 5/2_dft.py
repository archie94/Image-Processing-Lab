"""
Find 2-DFT and Amplitude spectrum in the given image
		3 6 2 4
		1 5 7 9
		3 5 9 2
		1 2 6 7
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img =np.array([3,6,2,4,1,5,7,9,3,5,9,2,1,2,6,7]).reshape(4,4)

dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
dft = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft[:,:,0],dft[:,:,1]))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('2-DFT image'), plt.xticks([]), plt.yticks([])
plt.show()
