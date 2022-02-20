import cv2
import os

video = cv2.VideoCapture(0)
#downscale video resolution
video.set(3, 320)
video.set(4, 240)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

names = []

#contain all our users into one array
for users in os.listdir("dataset"):
    names.append(users)


while True:

    _, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor = 1.1, minNeighbors = 5)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
        id, _ = recognizer.predict(gray_frame[y:y+h, x:x+w])
        if id:
            cv2.putText(frame, names[id-1], (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
        else:
            cv2.putText(frame, 'Intruder', (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow("Video Feed", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()