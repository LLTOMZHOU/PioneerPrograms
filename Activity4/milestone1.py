import cv2
import numpy as np

cam = cv2.VideoCapture(0)
ret, prevFrame = cam.read()

kWid = 7
kHgt = 7

while True and ret:
    ret, frame = cam.read()

    # Preserve a copy of the current frame without any image processing for the next loop
    frameCopy = frame.copy()
    prevFrameCopy = prevFrame.copy()

    # frameCopy = cv2.cvtColor(frameCopy, cv2.COLOR_BGR2GRAY)
    # prevFrameCopy = cv2.cvtColor(prevFrameCopy, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(prevFrameCopy, frameCopy)

    diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    cv2.imshow("raw difference in grayscale", diff)

    # diff remains to be the the raw comparison
    # med will be used for further image processing and display
    med = diff.copy()
    med = cv2.GaussianBlur(med, (kWid, kHgt), 0)
    ret, med = cv2.threshold(med, 25, 255, cv2.THRESH_BINARY)

    # Apply a morphological change
    st = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13))
    med = cv2.morphologyEx(med, cv2.MORPH_OPEN, st)


    cv2.imshow("after image processing", med)

    img, contrs, hier = cv2.findContours(med, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frameCopy, contrs, -1, (0, 255, 0), 3)

    cv2.imshow("output of cv2.finContours", img)
    cv2.imshow("Motion tracking", frameCopy)

    x = cv2.waitKey(20)
    c = chr(x&0xff)
    if c == 'q':
        break

    prevFrame = frame

cam.release()
cv2.destroyAllWindows()

