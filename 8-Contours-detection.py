import cv2 as cv
import numpy as np

img = cv.imread("assets/images/mountain.jpeg")

blank = np.zeros(img.shape, dtype='uint8')


# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)

# cv.imshow("blurred", blur)

# cany = cv.Canny(blur, 235, 175)
# cv.imshow("Canny", cany)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
rat, thresh =cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
contours, hierachires = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))
cv.drawContours(blank, contours, -1, (255,255,0), 2)
cv.imshow("Thresold", blank)

cv.waitKey(0)