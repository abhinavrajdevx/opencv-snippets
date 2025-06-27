import cv2 as cv
import numpy as np

blank = np.zeros([400,400], dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

bitsie_and = cv.bitwise_and(circle, rectangle)
bitsie_or = cv.bitwise_or(rectangle, circle)
bitsie_xor = cv.bitwise_xor(rectangle, circle)
bitsie_not = cv.bitwise_not(circle)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)
cv.imshow("bitsie_and", bitsie_and)
cv.imshow("bitsie_or", bitsie_or)
cv.imshow("bitsie_xor", bitsie_xor)
cv.imshow("bitsie_not", bitsie_not)

cv.waitKey(0)