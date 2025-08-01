import cv2 as cv
import numpy as np


img = cv.imread("assets/images/mountain.jpeg")
blank = np.zeros(img.shape[:2], dtype='uint8')

cv.imshow("original", img)
cv.imshow("Blank", blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 300, 255, -1)
cv.imshow("mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked", masked)

cv.waitKey(0)