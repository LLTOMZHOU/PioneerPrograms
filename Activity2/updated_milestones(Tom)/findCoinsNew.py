import numpy as np
import cv2

#Since the coins pictures provided all have some certain background intensity, I can filter them out.
origImg = cv2.imread("coins3.jpg")
# origImg = cv2.resize(origImg, None, fx = 0.4, fy = 0.4)
grayImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)

kWid = 7 #has to be odd
kHeight = 7 #has to be odd

# cv2.imshow("Gray Image original",grayImg)

### Perfoms several blurs and morphological filters
n = 1 #n <= 3
for nn in range(n):
    grayImg = cv2.GaussianBlur(grayImg, (kWid-nn*2, kHeight-nn*2), 0)

cv2.imshow("Gray Image blurred",grayImg)

# Take four pixels at the border to determine the average background intensity

height, width, depth = origImg.shape
# print (height, width)
bgIntensity = (grayImg[2,2]//4 + grayImg[height-1, width-1]//4 + grayImg[height-1, 2]//4 + grayImg[2, width-1]//4)

#### Filter out the background intensity ###
#The implementation is skipped as I came up with a simpler and better way do to this whole programs.
####

# binaryImg = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 3)
binaryImg = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3)

st = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
n = 10 #the number of iterations done to the grayscale image
for num in range(n):
    binaryImg = cv2.morphologyEx(binaryImg, cv2.MORPH_CLOSE, st)

cv2.imshow("binary image blurred", binaryImg)

# This works pretty well, but somehow very slow
# blueImg, greenImg, redImg = cv2.split(origImg)
# newImg = np.zeros((height, width, 3), dtype = np.uint8)
# # if a pixel is not of bgColor, set it to zero. Otherwise, set it to 255
# for i in range(height):
#     for j in range(width):
#         for n in range(3):
#             # print("evaluating")
#             if origImg[i,j,n] < bgColor[n] + 60 and origImg[i,j,n] > bgColor[n]-60:
#                 newImg[i,j,n] = 0
#             else:
#                 newImg[i,j, n] = 255
#
#             if newImg[i,j,0 ] == newImg[i,j,1] and newImg[i,j,2] == newImg[i,j,1] and newImg[i,j,1] == 0:
#                 pass
#             else:
#                 newImg[i,j,0] = 255
#                 newImg[i, j, 1] = 255
#                 newImg[i, j, 2] = 255
#                 # cv2.imshow("GrayScale image", grayImg)
# cv2.imshow("Filtering out the background color",newImg)


#Produce a grayscale image from a BGR(binary in nature) image for findContours to evaluate.
# grayNewImg = cv2.cvtColor(newImg, cv2.COLOR_BGR2GRAY)

# print(binaryImg[0][0])
# print(type(binaryImg))

img, contrs, hier = cv2.findContours(binaryImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(origImg, contrs, -1, (0, 255, 0), 3)

cv2.imshow("Coins detected", origImg)
cv2.waitKey(30000)