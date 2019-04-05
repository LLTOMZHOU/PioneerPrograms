import numpy as np
import cv2
import tkinter

#Since the coins pictures provided all have some certain
origImg = cv2.imread("coins6.jpg")
origImg = cv2.resize(origImg, None, fx = 0.4, fy = 0.4)

grayImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2GRAY)