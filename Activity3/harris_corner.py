import numpy as np
import cv2

origImg = cv2.imread("SampleImages/PuzzlesAndGames/puzzle4.png")
if origImg is None:
    print("Image not loaded successfully, try again")

#Preparing for harris detection
grayImg =cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)
grayImg = np.float32(grayImg)

dst = cv2.cornerHarris(grayImg, 2, 3, 0.04)#Function outputs another grascale image

#dilate and thresholding to show the importatn corners
dilDst = cv2.dilate(dst, None)
# dilDst = dst
thresh = 0.02*dst.max()
ret, threshDst = cv2.threshold(dilDst,thresh, 255, cv2.THRESH_BINARY)

cv2.imshow("Harris after dilation", threshDst)
cv2.imshow("original image",origImg)
cv2.imshow("Original Harris output",dst)

cv2.waitKey(80000)

