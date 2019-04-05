import cv2
import numpy as np

origImg = cv2.imread("coins6.jpg")
grayImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)

cannyImg = cv2.Canny(grayImg, 100, 200)
cv2.imshow("Canny Edge Detection", cannyImg)

cv2.waitKey(30000)
