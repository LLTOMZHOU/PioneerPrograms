import cv2
import numpy as np

#preprocessing the object to be recognized

mug = cv2.imread("mug.jpg")
mug = cv2.resize(mug, None, fx = 0.2, fy = 0.2)


vidCap = cv2.VideoCapture(0)
orb = cv2.ORB_create()
bfMatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

for i in range(1200):
    ret, img = vidCap.read()#ret ==> boolean flag for s uccessfully capture or not; img ==> a still frame captured
    img = img[:,::-1,:]
    height, width, depth = img.shape

    if not ret:
        print("fails to access your camera")
        break
### ORB
    kp1, des1 = orb.detectAndCompute(img, None)
    kp2, des2 = orb.detectAndCompute(mug, None)

    matches = bfMatcher.match(des1, des2)
    matches.sort(key = lambda x: x.distance)

    for num in range(len(matches)):
        if matches[num].distance > 40.0:
            break

    imgORB = cv2.drawMatches(img, kp1, mug, kp2, matches[:num], None)

    cv2.imshow("VideoStreaming", img)
    cv2.imshow("ORB detection and object matching",imgORB)

### Stop conditions
    stopKey = cv2.waitKey(12)
    keyChar = chr(stopKey & 0xff)
    if keyChar == "q":
        break
    elif keyChar == "s":
        cv2.imwrite("snapshot.jpg", img[:,::-1,:])

cv2.destroyAllWindows()
vidCap.release()
