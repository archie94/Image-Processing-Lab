# Discrete Cosine Transform

import numpy as np 
import cv2
import matplotlib.pyplot as plt 
import math
import copy

img = cv2.imread('../../Image/lena.jpg', 0)

# Change DCT of image by blurring the image 
for i in xrange(1,31,2):
   blur = cv2.blur(img,(i,i))
   string = 'blur : kernel size - '+str(i)

   imf = np.float32(blur)  # float conversion
   dst = cv2.dct(imf)           # the dct
   img2 = np.uint8(dst)    # convert back

   cv2.putText(blur,string,(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0))
   #vis = np.hstack([vis,np.hstack([blur,img2])])
   vis = np.concatenate((blur, img2), axis = 1)
   cv2.imshow('Blur',vis)
   cv2.waitKey(1000)
cv2.waitKey(0)