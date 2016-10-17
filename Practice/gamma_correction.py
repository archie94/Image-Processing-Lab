# Gamma correction and Power Law Transformation on RGB images
# http://www.pyimagesearch.com/2015/10/05/opencv-gamma-correction/

import cv2
import numpy as np 
from matplotlib import pyplot as plt 
import math
import copy

def adjust_gamma(img, gamma = 1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	inv_gamma = 1.0/gamma
	table = np.array([((i/255.0) ** inv_gamma) * 255 
		for i in np.arange(0, 256)]).astype("uint8")

	# apply gamma correction using lookup table
	return cv2.LUT(img, table)

img = cv2.imread('../Image/lena.jpg')

original = copy.copy(img)

# loop over various values of gamma
for gamma in np.arange(0.0, 3.5, 0.5):
	if gamma == 1:
		continue;

	gamma = gamma if gamma>0 else 0.1
	adjusted = adjust_gamma(original, gamma = gamma)
	cv2.putText(adjusted, "g={}".format(gamma), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	cv2.imshow("Images", np.hstack([original, adjusted]))
	cv2.waitKey(0)
