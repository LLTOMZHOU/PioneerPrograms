import cv2
import numpy as np

vidCap = cv2.VideoCapture(0)



prevFrame = []
for i in range(5):
    anything, image = vidCap.read()
    prevFrame.append(image)
# print(prevFrame)

while True:
    ret, img = vidCap.read()#ret ==> boolean flag for successfully capture or not; img ==> a still frame captured
    if not ret:
        print("fails to access your camera")
        break

    #Update the prevFrame list
    prevFrame.append(img)
    prevFrame = prevFrame[-5:]

    # cv2.imshow("hhh",prevFrame[0])
    img = cv2.addWeighted(img, 0.7, prevFrame[0], 0.3, 0)
    print(prevFrame[0])
    cv2.imshow("VideoStreaming", img[:,::-1,:])
    stopKey = cv2.waitKey(12)
    keyChar = chr(stopKey & 0xff)
    if keyChar == "q":
        break
    elif keyChar == "s":
        cv2.imwrite("snapshot.jpg", img[:,::-1,:])

cv2.destroyAllWindows()
vidCap.release()
