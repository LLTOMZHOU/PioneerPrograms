import cv2
import numpy
import time

#### Selecting a mode to import the image,
grayImg = cv2.imread("chicago.jpg", cv2.IMREAD_GRAYSCALE) #this is how to directly convert from BGR to GRAY
# print(cv2.IMREAD_GRAYSCALE)
# print(type(cv2.IMREAD_GRAYSCALE)) ##this is just an integer 'flag'
# print(type(img))
cv2.imshow("Grayscale", grayImg)
cv2.waitKey(9000)
#cv2.imwrite("chicago_grayscale.jpg", grayImg)


#### Importing an image and then converting between color spaces
snowLeo2 = cv2.imread("snowLeo2.jpg")
graySnowLeo2 = cv2.cvtColor(snowLeo2, cv2.COLOR_BGR2YUV)
cv2.imshow("Converted to YUV", graySnowLeo2)
cv2.waitKey(9000)


####Show separate BGR channels of an image
def showBGRchannels(img_object):
    cv2.imshow("Red Channel",img_object[:,:,2]) # Red channel intensity
    cv2.waitKey(30000)
    cv2.imshow("Green Channel",img_object[:,:,1])
    cv2.waitKey(30000)
    cv2.imshow("Blue Channel",img_object[:,:,0])
    cv2.waitKey(30000)


#mightyMidway = cv2.imread("mightyMidway.jpg")
mushroom = cv2.imread("mushrooms.jpg")
mushroom_mod = cv2.imread("mushroom_modified.png")
showBGRchannels(mushroom_mod)


