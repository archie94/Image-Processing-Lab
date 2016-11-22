import cv2
import matplotlib.pyplot as plt 
import cv2
import numpy as np 
import copy

img = cv2.imread('../../Image/screenshot.png', 0)

# convert to black and white image 
thres,im_bw = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
img = cv2.threshold(img, thres, 255, cv2.THRESH_BINARY)[1]

kernel = np.array([[1, 0, 0], [0, 1, 1], [0, 1, 1]]) # kernel of hit or miss
# kernel = kernel + np.array( [[1, 1, 1], [1, 1, 1], [1, 1, 1]] )

out1 = out2 = copy.copy(img)
img_hm = cv2.filter2D(img, -1, kernel)

for i in range(0, img.shape[0]):
	for j in range(0, img.shape[1]):
		if(img[i,j]==255 or img_hm[i,j]==255):
			out1[i,j]=255
		else:
			out1[i,j]=0
		# out2[i,j]=img2[i,j]-img_hm[i,j]

out2 = cv2.subtract(img, img_hm)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(out1, cmap = 'gray')
plt.title('Thickenning'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(out2, cmap = 'gray')
plt.title('Thinning'), plt.xticks([]), plt.yticks([])
plt.show()