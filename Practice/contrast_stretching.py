import numpy as np 
import math
import cv2

# open image and convert to grayscale
image = cv2.imread('../Image/low_contrast.jpg', 0)

# find max and min pixel values
a = int(image.max())
b = int(image.min())

# convert image to float
c = image.astype(float)

# contrast stretching operation
out_image = 255 * (c-a)/(b-a)

# convert back to int
out_image = out_image.astype(int)

cv2.imwrite( '../Output/low_contrast.png', out_image)
cv2.destroyAllWindows()