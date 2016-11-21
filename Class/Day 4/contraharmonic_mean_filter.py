# http://www.slideshare.net/sardaralam1/filters-for-noise-in-image-processing
# https://diptutor.wordpress.com/2010/08/02/contraharmonic-mean-filter/

import cv2
import matplotlib.pyplot as plt 
import math
import numpy as np 
import copy

img = cv2.imread('../../Image/do_mean.png', 0)

out_img = copy.copy(img)

rows,cols=img.shape

si=1
Q=1

for i in range(1,rows):
	for j in range(1,cols):
		con=0
		s1=0
		s2=0
		for x in range(i-si, i+si+1):
			for y in range(j-si,j+si+1):
				if(x>0 and y>0 and x<rows and y<cols):
					con = con +1
					s1 = s1 + (img[x,y]**Q)
					s2 = s2 + (img[x,y]**(Q+1))
		out_img[i,j] = s2/s1 


plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(out_img, cmap = 'gray')
plt.title('Contra harmonic filter'), plt.xticks([]), plt.yticks([])
plt.show()
