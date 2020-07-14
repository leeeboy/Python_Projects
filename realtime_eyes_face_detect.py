
import numpy as ns
import cv2
faceCascade=cv2.CascadeClassifier('C:\\python3.7\\haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('C:\\python3.7\\haarcascade eye.xml')
#imports haar classifiers for face  and eye detection
vs=cv2.VideoCapture(0)
while True:
    ret,frame=vs.read()
    if frame is None:
        break
    faces = faceCascade.detectMultiScale(frame)

    for(x,y,w,h) in faces:#detects the points of the captured video
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        roi_color=frame[y:y+h,x:x+w]

        eyes=eye_cascade.detectMultiScale(frame)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,eh),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('Video',frame)#displays the output
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):#when 'q' is entered in keyboard the video stops 
        break

cv2.destroyAllWindows()#closes the window when q is pressed
