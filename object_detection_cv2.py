# Detect the objects  

import cv2

import numpy as np

cap = cv2.VideoCapture(r"C:\Users\pinak\OneDrive\Desktop\A VSCODE\OPEN CV2\los_angeles.mp4")

_, frame = cap.read()

cv2.imshow("Frame", frame)
cv2.waitKey(0)

#-----------------------------------

# video is nothing 1 image after another image
# if i press key then it keep goes to the next frame.

import cv2

import numpy as np

cap = cv2.VideoCapture(r'C:\Users\pinak\OneDrive\Desktop\A VSCODE\OPEN CV2\los_angeles.mp4')

while True:
    _, frame = cap.read()
    cv2.imshow("Frame", frame)
    cv2.waitKey(0)

#--------------------------------------
    
# it will display the complete video

import cv2

import numpy as np

cap = cv2.VideoCapture(r"C:\Users\kdata\Desktop\KODI WORK\0. DATASCIENCE PROJECT\8. Object tracking from scratch\Object-tracking-from-scratch-source_code\source_code\los_angeles.mp4")

while True:
    _, frame = cap.read()
    
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
