import cv2 as cv

img = cv.imread("assets/images/mountain.jpg")

cv.imshow("Cat", img)

# Convert Image to greyscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Blur a image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)


#Edge casscade
cany = cv.Canny(blur, 125,175)
# cv.imshow("cany", cany)

# Dialating a image
dialeted = cv.dilate(cany, (3,3), iterations=3)
cv.imshow("dialeted", dialeted)

# Eroding a aimage
eroded = cv.erode(dialeted, (3,3), iterations=3)
cv.imshow("eroded", eroded)
cv.waitKey(0)