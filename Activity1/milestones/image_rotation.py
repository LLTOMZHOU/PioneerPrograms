import  cv2
import numpy as np

img = cv2.imread("mushrooms.jpg")
numRows, numCols = img.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D