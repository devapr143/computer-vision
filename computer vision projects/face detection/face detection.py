import cv2
facecascade=cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,640)
cap.set(10,150)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(imgGray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(20,255,57),2)
        cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break