import cv2 as cv 

img = cv.imread('Cat_Picture\kittens.jpg')

cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

#cv.findContours looks at edges (canny) and returns 2 values
#contours are python lists of all coords of contours found in the image
#hierarchies ranks contours by value
#cv.RETR_LIST returns all contours found in the images
#cv.CHAIN_APPROX_NONE is the approximation method 


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) 

print("There are {0} contours in this image!".format(len(contours)))

cv.waitKey(0)
