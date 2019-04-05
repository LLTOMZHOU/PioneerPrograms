import cv2
import numpy as np

catImg = cv2.imread("snowLeo2.jpg")

#drawing a circle aroung its head
cv2.circle(catImg, (125, 140), 64, (0,0,255), 5)

#Drawing a filled-in rectangle around its body
cv2.rectangle(catImg, (270, 145), (430, 260), (0, 255, 0), -1)
#Drawing a series of lines down its tail
cv2.line(catImg, (560, 130), (590, 240), (255, 0, 0), 4)
cv2.line(catImg, (590, 240), (600, 300), (255, 0, 0), 4)
#drawing a filename at top-left corner

font = cv2.FONT_HERSHEY_SIMPLEX
print(type(font))
cv2.putText(catImg, "snowLeo2.jpg",(10,30), font, 1, (255,255,255))

cv2.imshow("mark_up_version", catImg)
cv2.waitKey(10000)