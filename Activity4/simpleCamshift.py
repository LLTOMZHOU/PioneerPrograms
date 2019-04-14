#!/usr/bin/env python


import numpy as np
import cv2

showBackProj = False
showHistMask = False
frame = None
hist = None



def show_hist(hist):
    """Takes in the histogram, and displays it in the hist window."""
    bin_count = hist.shape[0]
    bin_w = 24
    img = np.zeros((256, bin_count * bin_w, 3), np.uint8)
    for i in range(bin_count):
        h = int(hist[i])
        cv2.rectangle(img, (i * bin_w + 2, 255), ((i + 1) * bin_w - 2, 255 - h), (int(180.0 * i / bin_count), 255, 255),
                      -1)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imshow('hist', img)



cam = cv2.VideoCapture(0)
ret, frame = cam.read()

if frame is not None:
    (hgt, wid, dep) = frame.shape
    # frame = cv2.resize(frame, dsize = (0, 0), fx = 0.5, fy = 0.5)
    # frame = getNextFrame(cam)
    cv2.namedWindow('camshift')
    cv2.namedWindow('hist')
    cv2.moveWindow('hist', 700, 100)  # Move to reduce overlap

    # Initialize the track window to be the whole frame
    track_window = (0, 0, wid, hgt)

    # Initialize the histogram from the stored image
    # Here I am faking a stored image with just a couple of blue colors in an array
    # you would want to read the image in from the file instead
    histImage = np.array([[[110, 70, 50]],
                          [[111, 128, 128]],
                          [[115, 100, 100]],
                          [[117, 64, 50]],
                          [[117, 200, 200]],
                          [[118, 76, 100]],
                          [[120, 101, 210]],
                          [[121, 85, 70]],
                          [[125, 129, 199]],
                          [[128, 81, 78]],
                          [[130, 183, 111]]], np.uint8)
    maskedHistIm = cv2.inRange(histImage, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
    hist = cv2.calcHist([histImage], [0], maskedHistIm, [16], [0, 180])
    cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
    hist = hist.reshape(-1)
    show_hist(hist)

    # start processing frames
    while True:
        ret, frame = cam.read()
        vis = frame.copy()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # convert to HSV
        mask = cv2.inRange(hsv, np.array((0., 60., 32.)),
                           np.array((180., 255., 255.)))  # eliminate low and high saturation and value values


        # The next line shows which pixels are being used to make the histogram.
        # it sets to black all the ones that are masked away for being too over or under-saturated
        if showHistMask:
            vis[mask == 0] = 0

        prob = cv2.calcBackProject([hsv], [0], hist, [0, 180], 1)
        prob &= mask
        term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
        track_box, track_window = cv2.CamShift(prob, track_window, term_crit)

        if showBackProj:
            vis[:] = prob[..., np.newaxis]
        try:
            cv2.ellipse(vis, track_box, (0, 0, 255), 2)
        except:
            print("Track box:", track_box)

        cv2.imshow('camshift', vis)

        ch = chr(0xFF & cv2.waitKey(5))
        if ch == 'q':
            break
        elif ch == 'b':
            showBackProj = not showBackProj
        elif ch == 'v':
            showHistMask = not showHistMask

cv2.destroyAllWindows()


