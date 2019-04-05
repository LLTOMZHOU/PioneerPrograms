import cv2
import numpy as np

for i in range(4):
    name = "snowLeo" + str(i+1) +".jpg"
    img = cv2.imread(name)
    cv2.imshow("Images", img)
    cv2.waitKey(10000)


