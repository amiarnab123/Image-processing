import cv2
import numpy as np

img = cv2.imread('Liu Bolin.jpg')

imgBlue = img[:,:,0]
imgGreen = img[:,:,1]
imgRed = img[:,:,2]

img = np.hstack((imgBlue,imgGreen,imgRed))

cv2.imshow("window",img)

cv2.waitKey(0)