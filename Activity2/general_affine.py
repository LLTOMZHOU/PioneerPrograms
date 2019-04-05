import cv2
import numpy as np

img1 = cv2.imread("snowLeo2.jpg")
rowNum, colNum = img1.shape[:2] # first two dimensions of a three dimensional array

#translate: x +10  y + 70
origPts = np.float32([[40,40],[160,40],[40,160]])
newPts = np.float32([[10,80],[180,5],[35,193]])


affine_matrix = cv2.getAffineTransform(origPts, newPts)

img1_affine = cv2.warpAffine(img1, affine_matrix, (colNum , rowNum)) #Notice the colNum is in front

cv2.imshow("Translation of img", img1_affine)
cv2.waitKey()
cv2.destroyAllWindows()
