import cv2
import numpy as np
img=cv2.imread("Resources/cards.jpg")
width,height=250,350
pts1=np.float32([[266,47],[423,74],[234,272],[390,297]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
outputimage=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("output",outputimage)

cv2.imshow("image",img)
cv2.waitKey(0 )