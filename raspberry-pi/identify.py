import cv2

video = cv2.VideoCapture(0)
video.set(3, 320)
video.set(4, 240)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    _, frame = video.read()

    faces = face_cascade.detectMultiScale(frame, 
    scaleFactor = 1.1,
    minNeighbors = 5)

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0))

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()