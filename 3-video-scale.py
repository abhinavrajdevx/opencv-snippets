import cv2 as cv 

def scaleframe(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimesnions = (width, height)
    return cv.resize(frame, dimesnions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("assets/videos/cat.mp4")

while True :
    isTrue, frame = capture.read()
    frame_resized = scaleframe(frame, 0.5)

    cv.imshow("Resized Video", frame_resized)
    cv.imshow("Video", frame)

    if cv.waitKey(30) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
