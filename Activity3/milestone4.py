import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
# print(type(face_cascade))

googley = cv2.imread("GoogleyEye.png")

if googley is None:
    print("Image not loaded successfully, try again")

vidCap = cv2.VideoCapture(0)
for i in range(1200):
    ret, img = vidCap.read()#ret ==> boolean flag for s uccessfully capture or not; img ==> a still frame captured
    if not ret:
        print("fails to access your camera")
        break

    img = img[:,::-1,:]
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    height, width, depth = img.shape
    # print(img.shape)
    HaarImg = img.copy()  # HaarImg is basically a copy of original frame
    face_rects = face_cascade.detectMultiScale(imgGray, 1.3, 5)

    # print(face_rects)
    for (x,y,w,h) in face_rects:
        # Somehow, I had to use origImg instead of img here, otherwise opencv reports an error
        cv2.rectangle(HaarImg, (x, y), (x + w, y + h), (0, 255, 0), 3)
        # cv2.rectangle(origImg, (50, 20), (300, 300), (0, 255, 0), 3)

        ROI = HaarImg[y:y+h, x:x+w]
        grayROI = imgGray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(grayROI, 1.3, 5)

        for (x_eye, y_eye, w_eye, h_eye) in eyes:
            googley = cv2.resize(googley, (w_eye, h_eye))
            googleyGray = cv2.cvtColor(googley, cv2.COLOR_BGR2GRAY)

            gHeight, gWidth, gDepth = googley.shape
            #No matter what happened to the size of googleyEye, the ROI should be the same size
            eyeROI = ROI[y_eye:y_eye+gHeight, x_eye:x_eye + gWidth]


            ret, mask = cv2.threshold(googleyGray, 240, 255, cv2.THRESH_BINARY_INV)
            mask_inv = cv2.bitwise_not(mask)


            tmp1 = cv2.bitwise_and(googley, googley, mask = mask)
            tmp2 = cv2.bitwise_and(eyeROI,eyeROI, mask = mask_inv)

            eyeROI = cv2.add(tmp1, tmp2)

            # cv2.imshow("eyeROI", eyeROI)
            ROI[y_eye:y_eye+gHeight, x_eye:x_eye + gWidth] = eyeROI
            #s omehow i needed the above step, since changing eyeROI alone doesn't affect ROI. humm
            # cv2.imshow("ROI", ROI)
            # print(mask)
            # center = (int(x_eye +0.5*w_eye), int(y_eye+0.5*h_eye))
            # radius = int(0.3* (w_eye + h_eye))
            # cv2.circle(ROI, center, radius, (0,255,0), 3)

    cv2.imshow("VideoStreaming", img)
    cv2.imshow("Face and eye detection", HaarImg)
    # cv2.imshow("Googley Eye", googley)

    stopKey = cv2.waitKey(12)
    keyChar = chr(stopKey & 0xff)
    if keyChar == "q":
        break
    elif keyChar == "s":
        cv2.imwrite("snapshot.jpg", img[:,::-1,:])

cv2.destroyAllWindows()
vidCap.release()
