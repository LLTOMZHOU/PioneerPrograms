import cv2
import numpy as np

img1 = cv2.imread("snowLeo2.jpg")
rowNum, colNum = img1.shape[:2] # first two dimensions of a three dimensional array

print(rowNum, colNum)
print(img1.shape)
img1 = cv2.resize(img1, None, fx = 1/2, fy = 1/2)

print("after resizing")
print(rowNum, colNum)
print(img1.shape)

#translate: x +10  y + 70
rotation_matrix = cv2.getRotationMatrix2D((colNum/2, rowNum/2), 30, 1) #rotate about the center of img1

img1_rotation = cv2.warpAffine(img1, rotation_matrix, (colNum, rowNum)) #Notice the colNum is in front

print(rotation_matrix)
cv2.imshow("Rotation of img", img1_rotation)
cv2.waitKey()

