import cv2 as cv
import numpy as np

img = cv.imread("assets/images/mountain.jpg")

# Translation
def translate (img, x, y):
    transmat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions)



# rotate
def rotate(img, angle, rotpoint=None):
    (height, width) = img.shape[:2]
    if rotpoint is None:
        rotpoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimsension = (width, height)
    return cv.warpAffine(img, rotMat, dimsension)

rotated = rotate(img, 10)
flip = cv.flip(rotated, 1)
cropped = flip[200:400, 300:500]
cv.imshow("Cat", cropped)

cv.waitKey(0)