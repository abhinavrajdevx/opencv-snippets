import cv2 as cv

img = cv.imread("assets/images/cat.jpeg")

cv.imshow("Cat", img)

cv.waitKey(0)