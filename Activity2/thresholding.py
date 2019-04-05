import numpy as np
import cv2

origImg = cv2.imread('coins6.jpg')

#Makes it easier for threshold function to process thresholds by converting to a grayscale image.
grayImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)
thres, threshImg = cv2.threshold(grayImg, 150, 255, cv2.THRESH_BINARY)

#everything below 150 is black and anything else will be white

print(thres)
# print(threshImg)

# print(cv2.THRESH_BINARY)

cv2.imshow("thresholded img", threshImg)

cv2.waitKey()
cv2.destroyAllWindows()