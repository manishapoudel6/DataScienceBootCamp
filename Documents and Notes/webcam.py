# use opencv to openwebcam for video and try background subtractor on that.

import numpy as np
import cv2

cap = cv2.VideoCapture("IMG_4922.MOV")
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    fgmask = fgbg.apply(frame)

    cv2.imshow('Original Frame', frame)
    cv2.imshow('Foreground Mask', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # Press 'Esc' key to exit
        break

cap.release()
cv2.destroyAllWindows()
