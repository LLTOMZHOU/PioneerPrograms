import numpy as np
import cv2

#Since the coins pictures provided all have some certain
origImg = cv2.imread("coins7.jpg")

grayImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)
height, width = grayImg.shape

grayImg = cv2.GaussianBlur(grayImg, (7, 7), 2)


bgIntensity = (grayImg[2,2]//4 + grayImg[height-1, width-1]//4 + grayImg[height-1, 2]//4 + grayImg[2, width-1]//4)
# print(bgIntensity)

thres, threshImg1 = cv2.threshold(grayImg, bgIntensity-55, 255, cv2.THRESH_BINARY_INV)
thres, threshImg2 = cv2.threshold(grayImg, bgIntensity+26, 255, cv2.THRESH_BINARY)
#
binaryImg = cv2.bitwise_or(threshImg1, threshImg2)
# binaryImg = threshImg1

st = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
n = 4 #the number of iterations done to the grayscale image
for num in range(n):
    binaryImg = cv2.morphologyEx(binaryImg, cv2.MORPH_DILATE, st)


circles = cv2.HoughCircles(binaryImg, cv2.HOUGH_GRADIENT, 1, 20, param1 = 40,
                           param2 = 15, minRadius = 60, maxRadius = 150)

print(circles.shape)

circles = circles[0]
print(circles.shape)

for circle in circles:
    coor = (int(circle[0]), int(circle[1]))
    cv2.circle(origImg, coor, int(circle[2]), (0,0,255), 5)


cv2.imshow("binaryCombined",binaryImg)
cv2.imshow("new",origImg)

cv2.waitKey(30000)