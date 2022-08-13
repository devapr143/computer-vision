import cv2

numberplatescascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minarea=500
color=(0,0,255)
count=0

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,1000)
while True:
    success, img= cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberplates = numberplatescascade.detectMultiScale(imgGray, 1.1, 4)
    for (x,y,w,h) in numberplates:
        area= w*h
        if area >minarea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(20,255,57),2)
            cv2.putText(img,"Number Plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX,0.5,color,2)
            imgRoi=img[y:y+h,x:x+w]
            cv2.imshow("Roi",imgRoi)
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("Resources/saves/NO.Plate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,150),(640,300),(80,255,20),cv2.FILLED)
        cv2.putText(img,"SAVED",(150,250),cv2.FONT_HERSHEY_DUPLEX,2,(255,255,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1