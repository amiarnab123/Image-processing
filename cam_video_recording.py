import numpy as np
import cv2
from time import sleep

cam = cv2.VideoCapture('output.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:

    ret,frame = cam.read()

    img_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(img_rgb)

    cv2.imshow('webcam',img_rgb)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break


out.release()
cv2.destroyAllWindows()