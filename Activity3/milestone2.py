import cv2
import numpy as np

vidCap = cv2.VideoCapture(0)
orb = cv2.ORB_create()
fast = cv2.FastFeatureDetector_create()

for i in range(1200):
    ret, img = vidCap.read()#ret ==> boolean flag for s uccessfully capture or not; img ==> a still frame captured
    img = img[:,::-1,:]
    height, width, depth = img.shape

    if not ret:
        print("fails to access your camera")
        break
### ORB
    keypoints, descriptors = orb.detectAndCompute(img, None)
    imgORB = cv2.drawKeypoints(img, keypoints, None, (255,0,0), 2)
####
### FAST
    keypts = fast.detect(img, None)
    imgFAST = cv2.drawKeypoints(img, keypts, None, (255,0,0), 2)
####
### Harris
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayImg = np.float32(grayImg)

    dst = cv2.cornerHarris(grayImg, 2, 3, 0.04)
    dilDst = cv2.dilate(dst, None)
    # dilDst = dst
    thresh = 0.01 * dst.max()
    ret, threshDst = cv2.threshold(dilDst, thresh, 255, cv2.THRESH_BINARY)

    threshDst = np.uint8(threshDst)
    threshDstInv = cv2.bitwise_not(threshDst)

    # Now threshDst acts like a mask. Any corners detected will be marked red.
    redColor = np.zeros((height, width, 3), np.uint8)
    redColor[:, :] = (0, 0, 255)

    redColor = cv2.bitwise_and(redColor, redColor, mask=threshDst)
    maskingHarris = cv2.bitwise_and(img, img, mask=threshDstInv)
    harrisOutput = cv2.add(redColor, maskingHarris)

    cv2.imshow("VideoStreaming", img)
    cv2.imshow("ORB detection",imgORB)
    cv2.imshow("FAST detection", imgFAST)
    cv2.imshow("Harris Corner", harrisOutput)

    stopKey = cv2.waitKey(12)
    keyChar = chr(stopKey & 0xff)
    if keyChar == "q":
        break
    elif keyChar == "s":
        cv2.imwrite("snapshot.jpg", img[:,::-1,:])

cv2.destroyAllWindows()
vidCap.release()

# Why does FAST detect more points than ORB?