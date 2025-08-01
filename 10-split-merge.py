import cv2 as cv
import numpy as np



img = cv.imread("assets/images/mountain.jpeg")
blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)

merged = cv.merge([b,g,r])
cv.imshow("Merged image", merged)

cv.imshow("Thresold", img)

cv.waitKey(0)