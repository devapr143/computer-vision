import cv2
import numpy as np
def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver
def getcontours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)

        if area>500:
            cv2.drawContours(imgcopy, cnt, -1, (200, 55, 155), 3)
            peri=cv2.arcLength(cnt,True)
            print(peri)
            approx =cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objcor=(len(approx))
            x,y,w,h=cv2.boundingRect(approx)
#add extra number of edges here as objcor and assign the name of
# shape as object type also remember to change the parameter for circle also
            if objcor ==3: objectType="Triangle"
            elif objcor ==4:
                aspRatio=w/float(h)
                if aspRatio>0.95 and aspRatio<1.05: objectType="Square"
                else:objectType="Rectangle"
            elif objcor>4:objectType="circle"
            else:objectType="none"
            cv2.rectangle(imgcopy,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(imgcopy,objectType,(x+(w//2)-15,y+(h//2)-15),cv2.FONT_HERSHEY_PLAIN,
                        1.2,(255,0,0),2)


path="Resources/shapes.png"
img=cv2.imread(path)
imgcopy=img.copy()
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)

getcontours(imgCanny)
imgBlank=np.zeros_like(img)

imgStack=stackImages(0.5,([img,imgGray,imgBlur],[imgCanny,imgcopy,imgBlank]))

cv2.imshow("Stack",imgStack)
#cv2.imshow("Original",img)
#cv2.imshow("Image Gray",imgGray)
#cv2.imshow("Inage Blur",imgBlur)

cv2.waitKey(0)