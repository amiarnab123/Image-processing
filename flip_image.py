import cv2
import numpy as np

img = cv2.imread('Liu Bolin.jpg')

img_flip = cv2.flip(img,1) # 0 means vertically flip and 1 means horizontally flip

cv2.imshow("window",img_flip)

print(img.shape)

cv2.waitKey(0)