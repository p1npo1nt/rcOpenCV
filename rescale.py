import cv2 as cv


img = cv.imread('Cat_Picture\cat.jpg')
cv.imshow('Cat', img)

#TAKES IN FRAME AND SCALES BY SCALE VALUE (0.75)
def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)   #frame.shape[1] width of image
    height = int(frame.shape[0] * scale)  #frame.shape[0] height of image
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

capture = cv.VideoCapture('Cat_Video\dog.mp4')

while True:
    isTrue, frame = capture.read() #reads video frame by frame

    frame_resized = rescaleFrame(frame) #0.75 scale value
   
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows