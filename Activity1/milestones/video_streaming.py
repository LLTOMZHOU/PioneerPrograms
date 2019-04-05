import cv2
import numpy as np

vidCap = cv2.VideoCapture(0)
for i in range(900):
    ret, img = vidCap.read()#ret ==> boolean flag for successfully capture or not; img ==> a still frame captured
    if not ret:
        print("fails to access your camera")
        break
    cv2.imshow("VideoStreaming", img[:,::-1,:])
    stopKey = cv2.waitKey(12)
    keyChar = chr(stopKey & 0xff)
    if keyChar == "q":
        break
    elif keyChar == "s":
        cv2.imwrite("snapshot.jpg", img[:,::-1,:])

cv2.destroyAllWindows()
vidCap.release()

