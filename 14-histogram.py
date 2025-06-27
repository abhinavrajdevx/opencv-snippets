import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("assets/images/mountain.jpeg")
blank = np.zeros(img.shape[:2], dtype='uint8')

cv.imshow("original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

ciecle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 300, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=ciecle)

cv.imshow("Mask", mask)

gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title("grayscale histogram")
plt.xlabel("bins")
plt.ylabel("no. of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)