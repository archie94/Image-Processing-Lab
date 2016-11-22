# Apply Adaptive local noise reduction filter 
import numpy as np 
import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('../../Image/gaussian1.png', 0)
img1 = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in xrange(4):
   plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()