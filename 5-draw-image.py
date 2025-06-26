import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
img = cv.imread("assets/images/cat.jpeg")

cv.rectangle(blank, (20,20), (250,200), (0, 255,0))
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=1)
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=100)

cv.putText(blank, "Abhinav Raj", (225,225), cv.FONT_HERSHEY_COMPLEX, 2.0, (0,255,255), thickness=2)

cv.imshow("Rectandle", blank)
cv.waitKey(0)