import cv2
import numpy as np

mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

if mouth_cascade.empty():
	raise IOError('Unable to load the mouth cascade classifier xml file')

cap = cv2.VideoCapture('trim1.mp4')
ds_factor = 0.5
i=0
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.3, 15)

    # print(len(mouth_rects))
    if len(mouth_rects) != 0:
        for (x,y,w,h) in mouth_rects:
            y = int(y - 0.15*h)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
            break
        frame = cv2.rotate(frame, cv2.cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite('mouth_test'+str(i)+'.jpg', frame)

        cv2.imshow('Mouth Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break
    i+=1
cap.release()
cv2.destroyAllWindows()
