import cv2
import numpy as np
import os

listImg = [obj for obj in os.listdir() if obj[-3:] == "jpg" or obj[-3:] == "png"]

for name in listImg:
    img = cv2.imread(name)
    cv2.imshow("Images", img)
    cv2.waitKey(10000)

