#pip install opencv-contrib-python
#pip install caer

import cv2 as cv

img = cv.imread('Cat_Picture\cat_large.jpg')

cv.imshow('Cat', img) #name of window, matrix type

cv.waitKey(0)


capture = cv.VideoCapture('Cat_Video\dog.mp4')

while True:
    istrue, frame = capture.read() #reads video frame by frame
    cv.imshow('Video', frame)

    

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows