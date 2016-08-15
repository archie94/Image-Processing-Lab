# Script to save the grayscale image of an image
import cv2

image = cv2.imread('../Image/3.jpg')
gray_img = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)

cv2.imwrite( '../Output/3_gray.jpg', gray_img) # save image to hdd ... directory should be present
cv2.imshow( 'Color Image', image)
cv2.imshow( 'Grayscale Image', gray_img)
cv2.waitKey(0) # waits forever for user to press any key
cv2.destroyAllWindows() # Closes displayed windows