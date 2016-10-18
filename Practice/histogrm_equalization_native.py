# Histogram Equalization done native way
# Follow this : https://en.wikipedia.org/wiki/Histogram_equalization

import cv2
from matplotlib import pyplot as plt 
import numpy as np 
import copy

img = cv2.imread('../Image/10.jpg', 0)

hist = {}
for i in range(0, img.shape[0]):
	for j in range(0, img.shape[1]):
		if img[i,j] in hist:
			hist[img[i,j]] = hist[img[i,j]] + 1
		else:
			hist[img[i,j]] = 1

cdf = {}
c = 0
for pixel in sorted(hist):
	c = c + hist[pixel]
	cdf[pixel] = c

# print hist
# print "==========="
# print cdf


cdf_min =  cdf[min(cdf.keys())]
M = img.shape[0]
N = img.shape[1]
L = 256 
h = {}

for pixel in cdf:
	h[pixel] = int(round(1.0 * (cdf[pixel] - cdf_min) / (M * N - cdf_min) * (L - 1)))

# print h

out_img = copy.copy(img)

for i in range(0, out_img.shape[0]):
	for j in range(0, out_img.shape[1]):
		out_img[i,j] = h[out_img[i,j]]

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(out_img, cmap='gray'), plt.title('Histogram Equalization')
plt.xticks([]), plt.yticks([])
plt.show()
