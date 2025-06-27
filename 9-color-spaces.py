import cv2 as cv
import numpy as np

img = cv.imread("assets/images/mountain.jpeg")



cv.imshow("Thresold", img)

cv.waitKey(0)