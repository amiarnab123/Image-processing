import cv2
import numpy as np

img = cv2.imread('Liu Bolin.jpg')

#img_resize = cv2.resize(img,(512,512))
img_resize = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))

cv2.imshow("window",img_resize)

print(img.shape)

cv2.waitKey(0)