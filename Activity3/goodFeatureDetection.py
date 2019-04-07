import numpy as np
import cv2

origImg = cv2.imread("SampleImages/PuzzlesAndGames/puzzle4.png")
if origImg is None:
    print("Image not loaded successfully, try again")

grayImg =cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)
grayImg = np.float32(grayImg)

goodFeats = cv2.goodFeaturesToTrack(grayImg, 400, 0.05, 3)

# print (goodFeats)
# print (goodFeats[1])
# print (goodFeats[0,0,0])

print(goodFeats.shape)

for feat in goodFeats:
    center = (feat[0,0], feat[0,1])
    cv2.circle(origImg, center, 3, (255,255,0), 1)

cv2.imshow("Corners detected", origImg)
cv2.waitKey(80000)