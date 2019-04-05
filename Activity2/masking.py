import numpy as np
import cv2

origImg = cv2.imread('coins6.jpg')

#Makes it easier for threshold function to process thresholds by converting to a grayscale image.
grayImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)
height, width = grayImg.shape

mask = np.zeros((height, width, 1), np.uint8)
mask[50:height//2, 50:width//2] = 255
maskedImg1 = cv2.bitwise_and(mask, grayImg)

#cv2.merge merges single channel imgs into multiple channel images
coloarMask = cv2.merge((mask, mask, mask))
maskedImg2 = cv2.bitwise_and(coloarMask, origImg) #note this time we use origImg

cv2.imshow("gray img", grayImg)
cv2.imshow("masked img one ", maskedImg1)
cv2.imshow("masked img two ", maskedImg2)

cv2.waitKey(9000)
cv2.destroyAllWindows()
