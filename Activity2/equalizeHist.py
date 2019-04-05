import cv2
import numpy as np
def grayscale():
    img1 = cv2.imread("snowLeo1.jpg")
    grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


    newGray1 = cv2.equalizeHist(grayImg1)
    cv2.imshow("grayImg", grayImg1)
    cv2.imshow("equalizedImg", newGray1)
    cv2.waitKey(8000)


def grayscale():
    img1 = cv2.imread("snowLeo1.jpg")
    grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    newGray1 = cv2.equalizeHist(grayImg1)
    cv2.imshow("grayImg", grayImg1)
    cv2.imshow("equalizedImg", newGray1)
    cv2.waitKey(8000)

if __name
