import cv2
import numpy as np

# create an image
img = np.zeros((512,512,3))

# Rectangle
cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3)
# Circle
cv2.circle(img,center=(200,200),radius=50,color=(0,0,255),thickness=2)
# Line
cv2.line(img,pt1=(0,0),pt2=(512,512),color=(0,255,0),thickness=2)
# Text
cv2.putText(img,text='Hello',org=(150,400),fontFace=cv2.FONT_ITALIC,fontScale=4,color=(0,255,255),thickness=2)

cv2.imshow("window",img)

print(img.shape)

cv2.waitKey(0)