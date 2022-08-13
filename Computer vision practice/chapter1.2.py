#resize crop
import cv2
import numpy as np
img=cv2.imread("Resources/yum.jpg")
print(img.shape)

imgresize = cv2.resize(img,(500,400))
print(imgresize.shape)
imgcropped=img[0:160,150:300 ]
cv2.imshow("cropped",imgcropped)
cv2.imshow("resized",imgresize)
cv2.imshow("Image",img)
cv2.waitKey(0)