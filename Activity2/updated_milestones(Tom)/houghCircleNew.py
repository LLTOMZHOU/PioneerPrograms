import numpy as np
import cv2


#Since the coins pictures provided all have some certain background intensity, I can filter them out.
origImg = cv2.imread("coins5.jpg")
# origImg = cv2.resize(origImg, None, fx = 0.4, fy = 0.4)
grayImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)

kWid = 5
kHeight = 5

# cv2.imshow("Gray Image original",grayImg)

### Perfoms several blurs and morphological filters
n = 5
for nn in range(n):
    grayImg = cv2.GaussianBlur(grayImg, (kWid, kHeight), 0)

st = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
n = 2 #the number of iterations done to the grayscale image
for num in range(n):
    grayImg = cv2.morphologyEx(grayImg, cv2.MORPH_OPEN, st)

cv2.imshow("Gray Image blurred",grayImg)

#Take one upper left pixel and thus determine the background color range.

height, width, depth = origImg.shape
# print (height, width)
bgIntensity = (grayImg[2,2]//4 + grayImg[height-1, width-1]//4 + grayImg[height-1, 2]//4 + grayImg[2, width-1]//4)

# Filter out the background intensity
binaryImg = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 3)
# binaryImg = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 3)


st = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
n = 4 #the number of iterations done to the grayscale image
for num in range(n):
    binaryImg = cv2.morphologyEx(binaryImg, cv2.MORPH_ERODE, st)

cv2.imshow("binary image blurred", binaryImg)

circles = cv2.HoughCircles(binaryImg, cv2.HOUGH_GRADIENT, 1, 20, param1 = 20,
                           param2 = 15, minRadius = 80, maxRadius = 120)

print(circles.shape)

circles = circles[0]
print(circles.shape)

for circle in circles:
    coor = (int(circle[0]), int(circle[1]))
    cv2.circle(origImg, coor, int(circle[2]), (0,0,255), 5)


cv2.imshow("binaryCombined",binaryImg)
cv2.imshow("new",origImg)

cv2.waitKey(30000)