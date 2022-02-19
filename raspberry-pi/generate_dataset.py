import cv2
from pathlib import Path

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

#downscale video resolution to ensure smooth fps on pi
video.set(3, 320)
video.set(4, 240)

print("Enter the id and name of the person: ")
userId = input()
userName = input()

count = 1 #used to see how many images we have saved

#method to save images
def saveImage(img, userName, userId, imgId):
    Path("dataset/{}".format(userName)).mkdir(parents=True, exist_ok = True)       #create folder to save images

while True:

    _, frame = video.read()

    originalFrame = frame


    faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 5)

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0))

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        saveImage(originalImg, userName, userId, count)
        count += 1
    elif key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()