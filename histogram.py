import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Cat_Picture\kittens.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#Grayscale histogram

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256]) #args: image


plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()
