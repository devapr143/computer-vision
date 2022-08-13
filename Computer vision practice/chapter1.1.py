#gray dialation erode blur
import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
img=cv2.imread("Resources/dev.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(11,11),0)
imgcanny=cv2.Canny(imgGray,100,150)
imgdialation=cv2.dilate(imgcanny,kernel,iterations=1)
imgeroded=cv2.erode(imgdialation,kernel,iterations=1)
cv2.imshow("img eroded",imgeroded)
cv2.imshow("img dilated",imgdialation)
cv2.imshow("GRAY Image",imgGray)
cv2.imshow("BLUR",imgBlur)
cv2.imshow("Canny(edges)",imgcanny)
cv2.waitKey(0)
