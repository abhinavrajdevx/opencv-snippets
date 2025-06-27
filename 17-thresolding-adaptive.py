import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("assets/images/mountain.jpeg")
cv.imshow("Cats",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive thresolding", adaptive_thresh)


cv.waitKey(0)