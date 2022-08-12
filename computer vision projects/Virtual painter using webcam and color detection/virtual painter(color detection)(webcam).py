
import cv2
import numpy as np
frameWidth = 960
frameHeight = 840
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
#to add colors to the painter add the parameters from color selector
#and add them mycolors list first three should be minimum values and they will go in lower and
#the next three will be maximum value and put them upper values
#enter respective color valuesfor your input colors
# for example:enter the BGR of purple at colorvalues[0] if your mycolors[0] is purple


myColors=[[105,64,164,129,131,255],[0,0,0,0,0,0],[1,1,1,1,1,1]]

colorvalues=[[255,0,255],[0,0,0],[255,255,255]]

mypoints= [] #[x,y,colorID]


def findcolor(img, myColors, colorvalues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newpoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getcontours(mask)
        cv2.circle(imgResult, (x, y), 15, colorvalues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newpoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]),mask)
    return newpoints

def getcontours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (0, 55, 255), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

def drawlines(mypoints, colorvalues):
    for point in mypoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, colorvalues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newpoints = findcolor(img, myColors, colorvalues)
    if len(newpoints) != 0:
        for newP in newpoints:
            mypoints.append(newP)
    if len(mypoints) != 0:
        drawlines(mypoints, colorvalues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break