import cv2
import numpy as np

###Applying histogram equalization, masking, and motion blurring to video
vidCap = cv2.VideoCapture(0)

def histEql(grayImg):
    newGray = cv2.equalizeHist(grayImg)
    return newGray

def motionBlur(img, ksize):
    kernel_motion_blur = np.zeros((ksize, ksize))
    kernel_motion_blur[int((ksize-1)/2), :] = np.ones(ksize)
    kernel_motion_blur = kernel_motion_blur/ksize

    newImg = cv2.filter2D(img, -1, kernel_motion_blur)
    return newImg

def masking(img, size):
    height, width, depth = img.shape
    mask = np.zeros((height, width, 1), np.uint8)

    #setting a square mask with length 2*size
    for i in range(height//2 - size, height//2 +size+1):
        for j in range(width//2 - size, width//2 + size+1):
            mask[i,j] = 255

    coloarMask = cv2.merge((mask, mask, mask))
    maskedImg = cv2.bitwise_and(coloarMask, img)

    return maskedImg


for i in range(900):
    ret, img = vidCap.read()#ret ==> boolean flag for successfully capture or not; img ==> a still frame captured
    if not ret:
        print("fails to access your camera")
        break
    #After intializing and getting the original image, convert it to grayscale for convenience
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Apply three different effects
    newGray = histEql(grayImg)
    motionBlurImg = motionBlur(img, 30)
    finalImg = masking(motionBlurImg, 150)


    cv2.imshow("VideoStreaming", finalImg[:,::-1,:])
    cv2.imshow("Higher contrast video in grayscale", grayImg[:,::-1])

    stopKey = cv2.waitKey(12)
    keyChar = chr(stopKey & 0xff)

    if keyChar == "q":
        break
    elif keyChar == "s":
        cv2.imwrite("snapshot.jpg", img[:,::-1,:])


cv2.destroyAllWindows()
vidCap.release()
