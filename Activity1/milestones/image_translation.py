import cv2
import numpy as np

img = cv2.imread("chicago.jpg")
numRows, numCols = img.shape[:2]

translation_matrix = np.float32([[1,0,70], [0,1,110]])
print(type(translation_matrix))
# 70 ==> x translation value 110 ==> y translation value
img_translation = cv2.warpAffine(img, translation_matrix, (numCols, numRows))
cv2.imshow("Translation", img_translation)

cv2.waitKey(12000)




