import numpy as np
import cv2

origImg = cv2.imread('coins6.jpg')
grayImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(grayImg, 127, 255, 0)

img, contrs, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print (hier)

cv2.drawContours(origImg, contrs, -1, (0, 255, 0), 3)
cv2.imshow("grayScale", grayImg)
cv2.imshow("Binary image",thresh)
cv2.imshow("contours", origImg)

cv2.waitKey()
cv2.destroyAllWindows()
