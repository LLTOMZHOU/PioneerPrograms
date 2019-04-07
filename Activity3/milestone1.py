import numpy as np
import cv2

origImg = cv2.imread("SampleImages/PuzzlesAndGames/puzzle4.png")
if origImg is None:
    print("Image not loaded successfully, try again")

height, width, depth = origImg.shape

# Preparing for harris detection
grayImg =cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)
grayImg = np.float32(grayImg)

dst = cv2.cornerHarris(grayImg, 2, 3, 0.04)  # Function outputs another grascale image

# dilate and thresholding to show the importatn corners
dilDst = cv2.dilate(dst, None)
# dilDst = dst
thresh = 0.02*dst.max()
ret, threshDst = cv2.threshold(dilDst,thresh, 255, cv2.THRESH_BINARY)

# Do a bitwiseand followed by a subtraction  to find out the corners
threshDst = np.uint8(threshDst)
threshDstInv = cv2.bitwise_not(threshDst)
# print(type(threshDst), type(grayImg))
# threshDst = cv2.bitwise_or(threshDst, grayImg)

# Now threshDst acts like a mask. Any corners detected will be marked red.
redColor = np.zeros((height, width, 3), np.uint8)
redColor[:,:] = (0, 0, 255)

redColor = cv2.bitwise_and(redColor, redColor, mask = threshDst)
maskingHarris = cv2.bitwise_and(origImg, origImg, mask = threshDstInv)
harrisOutput = cv2.add(redColor, maskingHarris)


goodFeats = cv2.goodFeaturesToTrack(grayImg, 400, 0.05, 3)
print(goodFeats.shape)
bkOrigImg = origImg.copy()

for feat in goodFeats:
    center = (feat[0,0], feat[0,1])
    cv2.circle(bkOrigImg, center, 3, (255,255,0), 1)


cv2.imshow("Harris after dilation", harrisOutput)
cv2.imshow("Original Img",origImg)
cv2.imshow("Good features to detect",bkOrigImg)
# cv2.imshow("Original Harris output",dst)

cv2.waitKey(80000)