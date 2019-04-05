import cv2
import numpy as np

img = cv2.imread("mushrooms.jpg")
img_scaled = cv2.resize(img, None, fx = 1.2, fy = 1.2, interpolation = cv2.INTER_LINEAR)
# img_scaled = cv2.resize(img, None, fx = 1.2, fy = 1.2, interpolation = cv2.INTER_CUBIC)
# img_scaled = cv2.resize(img, None, fx = 1.2, fy = 1.2, interpolation = cv2.INTER_AREA)

cv2.imshow("Original Photo", img)\
cv2.waitKey()

cv2.imshow("Linear Interpolation",img_scaled)
cv2.waitKey()
