import cv2

face_det = cv2.CascadeClassifier("C:/Users/Lenovo/miniconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml")
cam = cv2.VideoCapture(0)
while cam.isOpened():
    status, image = cam.read()
    col = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_det.detectMultiScale(col, scaleFactor= 1.1, minNeighbors = 5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow("Live Video", image)
    
    if cv2.waitKey(1) == 27:
        break
    
cam.release()