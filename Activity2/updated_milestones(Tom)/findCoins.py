import numpy as np
import cv2

#Since the coins pictures provided all have some certain
origImg = cv2.imread("coins6.jpg")
origImg = cv2.resize(origImg, None, fx = 0.2, fy = 0.2)

grayImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)

#Take one upper left pixel and thus determine the background color range.

height, width, depth = origImg.shape
# print (height, width)
bgColor = (origImg[2,2]//4 + origImg[height-1, width-1]//4 + origImg[height-1, 2]//4 + origImg[2, width-1]//4)
# print(bgColor)
blueImg, greenImg, redImg = cv2.split(origImg)
# print(blueImg, greenImg, redImg)

print(origImg.dtype)
newImg = np.zeros((height, width, 3), dtype = np.uint8)
# if a pixel is not of bgColor, set it to zero. Otherwise, set it to 255
for i in range(height):
    for j in range(width):
        for n in range(3):
            print("evaluating")
            if origImg[i,j,n] < bgColor[n] + 60 and origImg[i,j,n] > bgColor[n]-60:
                newImg[i,j,n] = 0
            else:
                newImg[i,j, n] = 255

            if newImg[i,j,0 ] == newImg[i,j,1] and newImg[i,j,2] == newImg[i,j,1] and newImg[i,j,1] == 0:
                pass
            else:
                newImg[i,j,0] = 255
                newImg[i, j, 1] = 255
                newImg[i, j, 2] = 255
                # cv2.imshow("GrayScale image", grayImg)

cv2.imshow("Filtering out the colors",newImg)

grayNewImg = cv2.cvtColor(newImg, cv2.COLOR_BGR2GRAY)
st = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
grayNewImg = cv2.morphologyEx(grayNewImg, cv2.MORPH_ERODE, st)
st = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
grayNewImg = cv2.morphologyEx(grayNewImg, cv2.MORPH_ERODE, st)

img, contrs, hier = cv2.findContours(grayNewImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(newImg, contrs, -1, (0, 255, 0), 3)

cv2.imshow("contours", newImg)

cv2.waitKey(30000)