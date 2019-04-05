import numpy as np
import cv2

origImg = cv2.imread('snowLeo4.jpg')

#Makes it easier for threshold function to process thresholds by converting to a grayscale image.
grayImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)
height, width = grayImg.shape

#compute gradient in horizontal direction (detect vertical edges)
sobelValsHorz = cv2.Sobel(grayImg, cv2.CV_32F, 1, 0)
horzImg = cv2.convertScaleAbs(sobelValsHorz)
cv2.imshow("horizontal gradient", horzImg)


#compute gradient in Vertical direction (detect honrizontal edges)
sobelValsVert = cv2.Sobel(grayImg, cv2.CV_32F, 0, 1)
vertImg = cv2.convertScaleAbs(sobelValsHorz)
cv2.imshow("vertical gradient", vertImg)

#Combining the two gradients
sobelComb = cv2.addWeighted(sobelValsHorz, 0.5, sobelValsVert, 0.5, 0)

sobelImg = cv2.convertScaleAbs(sobelComb)
cv2.imshow("Sobel", sobelImg)
cv2.waitKey(20000)
