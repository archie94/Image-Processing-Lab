# Mid point filter
# Best for Gaussian and uniform noise

import matplotlib.pyplot as plt 
import numpy as np 
import cv2
import math
import copy 

img = cv2.imread('../../Image/gaussian1.png', 0)
out_img = copy.copy(img)

row,col = img.shape

for i in range(1,row-1):
	for j in range(2,col-1):
		mx=img[i,j]
		mn=img[i,j]
		for x in range(i-1,i+2):
			for y in range(j-1,j+2):
				if(img[x,y]<mn):
					mn=img[x,y]
				if(img[x,y]>mx):
					mx=img[x,y]

		out_img[i,j] = mn+(mx-mn)/2;

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(out_img, cmap = 'gray')
plt.title('Mid point filter'), plt.xticks([]), plt.yticks([])
plt.show()
