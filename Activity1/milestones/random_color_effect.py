import cv2
import numpy as np
import random

for i in range(10):
    img = cv2.imread("chicago.jpg")
    channels = cv2.split(img)

    # print(channels.shape())
    random.shuffle(channels)

    # print(channels)
    print(type(channels))
    # print(channels)
    # print(type(channels))
    newImg = cv2.merge(channels)

    cv2.imshow("Random_color_effect", newImg)
    cv2.waitKey(9000)