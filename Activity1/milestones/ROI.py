import cv2
import numpy as np

catImg = cv2.imread("snowLeo1.jpg")
faceROI = catImg[250:550, 570:860] # doesn't copy data

cv2.imshow("original", catImg)
cv2.imshow("faceROI", faceROI)

cv2.waitKey(2000)

#Now manipulate the faceROI, setting the blue channel to 0
faceROI[:,:,1] = 0
cv2.imshow("original", catImg)
cv2.imshow("faceROI", faceROI)
cv2.waitKey()

flippedFace = faceROI[::-1, :, :]
cv2.imshow("flipped", flippedFace)
cv2.waitKey()

#Changing flippedFace also results in change in the original image
flippedFace[10:30,:,1] = 128
cv2.imshow("flipped", flippedFace)
cv2.imshow("original", catImg)
cv2.waitKey()