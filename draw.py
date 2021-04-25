#If you want to access OpenCV documentation, please visit this link: https://docs.opencv.org/master/

import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3), dtype='uint8') #creates blank image 
cv.imshow('Blank', blank) #shows blank image


#Paint the image a certain color (green)

blank[200:300, 300:400] = 0,255,0 #[:] references all pixels
cv.imshow('Green', blank)

#Draw a rectangle

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED) #cv.rectangle(img, vertex1, vertex2, color, thickness)

cv.imshow('Rectangle', blank)

cv.waitKey(0)