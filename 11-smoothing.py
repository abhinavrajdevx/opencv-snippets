import cv2 as cv
import numpy as np

img = cv.imread("assets/images/mountain.jpeg")
blank = np.zeros(img.shape[:2], dtype='uint8')



cv.imshow("Thresold", img)

cv.waitKey(0)