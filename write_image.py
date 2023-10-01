import cv2
import numpy as np

img = cv2.imread('Liu Bolin.jpg')

img_crop = img[0:300,0:300]

cv2.imwrite('cropped_image.jpg',img_crop)

cv2.imshow("window",img_crop)

print(img.shape)

cv2.waitKey(0)