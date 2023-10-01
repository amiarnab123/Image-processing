import numpy as np
import cv2
from time import sleep

cam = cv2.VideoCapture('output.avi')


while True:

    ret,frame = cam.read()
    
    sleep(1/20)
    cv2.imshow('webcam',frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break


cv2.destroyAllWindows()