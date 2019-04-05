import cv2
import numpy as np

pic = cv2.imread("coins6.jpg")

cv2.imshow("original image ", pic)

st = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
print("starting to apply morphological filters")

resultpic = cv2.morphologyEx(pic, cv2.MORPH_ERODE, st)
cv2.imshow("result image", resultpic)
cv2.waitKey(6000)
resultpic = cv2.morphologyEx(pic, cv2.MORPH_DILATE,st)
resultpic = cv2.morphologyEx(resultpic, cv2.MORPH_DILATE,st)
resultpic = cv2.morphologyEx(resultpic, cv2.MORPH_DILATE,st)

cv2.imshow("result image", resultpic)
cv2.waitKey(6000)

resultpic = cv2.morphologyEx(pic, cv2.MORPH_OPEN,st)
cv2.imshow("result image", resultpic)
cv2.waitKey(6000)
resultpic = cv2.morphologyEx(pic, cv2.MORPH_CLOSE,st)
cv2.imshow("result image", resultpic)
cv2.waitKey(6000)
resultpic = cv2.morphologyEx(pic, cv2.MORPH_BLACKHAT,st)
cv2.imshow("result image", resultpic)
cv2.waitKey(6000)
resultpic = cv2.morphologyEx(pic, cv2.MORPH_TOPHAT,st)
cv2.imshow("result image", resultpic)
cv2.waitKey(6000)

cv2.destroyAllWindows()






