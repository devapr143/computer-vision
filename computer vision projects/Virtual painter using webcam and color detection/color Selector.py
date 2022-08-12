import cv2
import numpy as np
frameWidth =360
frameHeight =360
cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty(a):
    pass
cv2.namedWindow("parameters")
cv2.resizeWindow("parameters",640,240)
cv2.createTrackbar("HUE Min", "parameters", 0, 179, empty)
cv2.createTrackbar("SAT Min", "parameters", 0, 255, empty)
cv2.createTrackbar("VALUE Min", "parameters", 0, 255, empty)
cv2.createTrackbar("HUE Max", "parameters", 179, 179, empty)
cv2.createTrackbar("SAT Max", "parameters", 255, 255, empty)
cv2.createTrackbar("VALUE Max", "parameters", 255, 255, empty)

while True:
    success, img=cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HUE Min", "parameters")
    h_max = cv2.getTrackbarPos("HUE Max", "parameters")
    s_min = cv2.getTrackbarPos("SAT Min", "parameters")
    s_max = cv2.getTrackbarPos("SAT Max", "parameters")
    v_min = cv2.getTrackbarPos("VALUE Min", "parameters")
    v_max = cv2.getTrackbarPos("VALUE Max", "parameters")

    lower =np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHsv,lower,upper)
    result= cv2.bitwise_and(img,img,mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack=np.hstack([img,mask,result])
    cv2.imshow("stack",hstack)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
cap.release()
cv2.destroyWindow()
