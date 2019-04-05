
import cv2
import numpy as np

uppLeft = None
lowLeft = None
uppRight = None
count = 0

def mouseResponse(event, x, y, flags, param):
    """This function is a callback that happens when the mouse is used.
    event describes which mouse event triggered the callback, (x, y) is
    the location in the window where the event happened. The other inputs
    may be ignored."""

    global uppLeft, lowLeft, uppRight, count

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(workImg, (x, y), 10, (75, 30, 30), -1)

        if count == 0:
            uppLeft = [x,y]
            print(x, y)
        elif count == 1:
            lowLeft = [x,y]
            print(x, y)
        elif count == 2:
            uppRight = [x,y]
            print(x,y)

        count += 1


# read in an image
origImg = cv2.imread("Exit1.jpg")
height, width, depth = origImg.shape

# make a copy and set up the window to display it
workImg = origImg.copy()
cv2.namedWindow("Working image")

# assign mouse_response to be the callback function for the Working image window
cv2.setMouseCallback("Working image", mouseResponse)

# Keep re-displaying the window, and look for user to type 'q' to quit
while True:
    cv2.imshow("Working image", workImg)
    x = cv2.waitKey(20)
    ch = chr(x & 0xFF)

    if count == 3:
        newPts = np.float32([[0,0],[0, height - 1],[width - 1, 0]]) #openCV uses (x,y), i.e. (width, height)
        origPts = np.float32([uppLeft, lowLeft, uppRight])
        affine_matrix = cv2.getAffineTransform(origPts, newPts)
        workImg = cv2.warpAffine(origImg, affine_matrix, (width, height))

    if ch == 'q':
        break

cv2.destroyAllWindows()
