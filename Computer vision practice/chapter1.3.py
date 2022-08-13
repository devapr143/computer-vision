#shapes and texts
#remove # from program according to need
import cv2
import numpy as np
img =np.zeros((512,512,3),np.uint8)
#print(img.shape)
#img[100:200,200:300]=255,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
cv2.rectangle(img,(0,10),(200,150),(125,20,58),10)
cv2.circle(img,(400,40),25,(0,255,255),4)
cv2.putText(img,"DEVA",(350,250),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,250),2)
cv2.imshow("image",img)
cv2.waitKey(0)