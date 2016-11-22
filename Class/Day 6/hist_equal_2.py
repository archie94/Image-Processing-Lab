"""
Let the two image f(x,y) and g(x,y) have histogram h(f) and h(g). Show the result for the following arithmetic operations between two histograms

	f(x,y) + g(x,y)
	f(x,y) - g(x,y)
	h(f) + h(g)
	h(f) - h(g) 
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

A = cv2.imread('../../Image/solt and pepar2.png', 0)
B = cv2.imread('../../Image/saltpepar2.png', 0)

a = cv2.addWeighted(A,1.0,B,1.0,0)
b = cv2.addWeighted(A,1.0,B,-1.0,0)

H1 = cv2.equalizeHist(A)
H2 = cv2.equalizeHist(B)

r1,c1 = H1.shape
r2,c2 = H2.shape

#print r1,c1
#print r2,c2

h1 = cv2.addWeighted(H1,1.0,H2,1.0,0)
h2 = cv2.addWeighted(H1,1.0,H2,-1.0,0)

"""
print H1
print '--------------------------------------------------'
print H2

print '=================================================='
print h1
print '--------------------------------------------------'
print h2



print A
print '--------------------------------------------------'
print B

print '=================================================='
print a
print '--------------------------------------------------'
print b
"""

titles = ['F', 'G', 'F + G', 'F - G',
'hist F + hist G', 'hist F - hist G']
images = [A, B, a, b, H1, H2]

for i in xrange(6):
   plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()