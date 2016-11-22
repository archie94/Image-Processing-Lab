import cv2
import matplotlib.pyplot as plt 
import cv2
import numpy as np 
import copy

img = cv2.imread('../../Image/shape.jpg', 0)

kernel = np.array([[0, 2, 2],[-2, 0 ,2],[-2,-2,0]]) # superimpose sobel x and y

out_img = cv2.filter2D(img, -1, kernel)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(out_img, cmap = 'gray')
plt.title('Boundary detection'), plt.xticks([]), plt.yticks([])
plt.show()
