# Alpha trimmed filter
#  This filter is useful for images containing multiple types of noise, such as gaussian and salt-undpepper noise. 
# https://www.scbaghdad.edu.iq/projects/computer/20072008/1.pdf

import cv2
import matplotlib.pyplot as plt 
import math
import copy
import numpy as np 

img = cv2.imread('../../Image/speckle.jpg', 0)
out_img = copy.copy(img)

rows,cols = img.shape

for i in range(1,rows-1):
	for j in range(1,cols-1):
		out_img[i,j]=img[j,i]

members = np.zeros(9)
alpha = 3

for i in range(1,rows-1):
	for j in range(1,cols-1):
		c=0;
		for x in range(i-1, i+2):
			for y in range(j-1,j+2):
				members[c] = img[x,y]
				c=c+1

		members.sort()
		summ=0
		for x in range(alpha,9-alpha):
			summ+=members[x]
		out_img[i,j]=summ/(9-2*alpha)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(out_img, cmap = 'gray')
plt.title('Alpha trimmed filter'), plt.xticks([]), plt.yticks([])
plt.show()
