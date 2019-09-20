import numpy as np
import cv2
from tracker import Tracker

cap = cv2.VideoCapture('final_edit.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2()


while True:
    
    ret, frame = cap.read()

    if ret == True:

        fgmask = fgbg.apply(frame)

        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    else:
        break
# while(1):
#     ret, frame = cap.read()

#     fgmask = fgbg.apply(frame)

#     cv2.imshow('frame',fgmask)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break

cap.release()
cv2.destroyAllWindows()



# while True:

#     ret, frame = cap.read()

#     if ret == True:

#         fgmask = fgbg.apply(frame)

#         cv2.imshow('frame',fgmask)
#         k = cv2.waitKey(30) & 0xff
#         if k == 27:
#             break

#     else:
#         break
