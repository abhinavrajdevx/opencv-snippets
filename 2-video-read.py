import cv2 as cv

capture = cv.VideoCapture("assets/videos/cat.mp4")

while True :
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    if cv.waitKey(300) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()