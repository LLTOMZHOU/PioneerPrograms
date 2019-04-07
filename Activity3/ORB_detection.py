import cv2
import numpy as np

origImg = cv2.imread("SampleImages/PuzzlesAndGames/puzzle7.png")
if origImg is None:
    print("Image not loaded successfully, try again")

height, width, depth = origImg.shape

orb = cv2.ORB_create()


# Image preprocessing
# keypts, descriptors = orb.detectAndCompute(img, None)

keypts = orb.detect(origImg, None)

keypoints, descriptors = orb.compute(origImg, keypts)

# print(keypoints)
# print(keypts)

imgOutput = cv2.drawKeypoints(origImg, keypts, None, (255, 0, 0), 2)  # Note the last parameter can influence how keypoints are displayed
# imgOutput = cv2.drawKeypoints(origImg, keypts, None, (255, 0, 0), 2)

cv2.imshow("output one", imgOutput)

cv2.waitKey(80000)

if keypoints == keypts:
    print("Yes, they are the same")
