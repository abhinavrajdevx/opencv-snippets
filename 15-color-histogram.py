import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("assets/images/cat.jpeg")
cv.imshow("Cats",img)

blank = np.zeros(img.shape[:2], dtype="uint8")

cv.imshow("original", img)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 40, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked", masked)

plt.figure()
plt.title("Color histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")


colors = ('b','g','r')
for i ,col in enumerate(colors):
    hist = cv.calcHist([img], [i] , mask,[256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)