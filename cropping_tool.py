import cv2
import numpy as np

flag = False
ix = -1
iy = -1

def crop(event,x,y,flags,params):

    global flag,ix,iy
    
    if event == 1:
        
        flag = True
        ix,iy = x,y

    elif event == 4:

        fx,fy = x,y

        flag = False
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,0),thickness=1)

        cropped_img = img[iy:fy,ix:fx]

        cv2.imshow('New window',cropped_img)


cv2.namedWindow('window')
cv2.setMouseCallback('window',crop)

img = cv2.imread('image.jpg')
while True:
    
    cv2.imshow('window',img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()