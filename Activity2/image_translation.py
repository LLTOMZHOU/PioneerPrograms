import cv2
import numpy as np

img1 = cv2.imread("snowLeo1.jpg")
rowNum, colNum = img1.shape[:2] # first two dimensions of a three dimensional array


#translate: x +10  y + 70
translation_matrix =np.float32([[1,0,20],[0,1,50]])
img1_translation = cv2.warpAffine(img1, translation_matrix, (colNum+30, rowNum)) #Notice the colNum is in front

cv2.imshow("Translation of img", img1_translation)
cv2.waitKey()


