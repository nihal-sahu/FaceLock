import cv2
from pathlib import Path

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

#downscale video resolution to ensure smooth fps on pi
video.set(3, 320)
video.set(4, 240)

print("\nPress 'q' to exit, press 's' to save an image to the dataset")
print("Enter the name of the person: ")

userName = input()

count = 1 #used to see how many images we have saved

#method to save images
def saveImage(img, userName, imgId):
    Path("dataset/{}".format(userName)).mkdir(parents=True, exist_ok = True)       #create folder to save images
    cv2.imwrite("dataset/{}/{}_{}.jpg".format(userName, userName, imgId), originalFrame)

while True:

    _, frame = video.read()

    originalFrame = frame


    faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 5)

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0))

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        #save only 20 images
        if count <= 20:
            saveImage(originalFrame, userName, count)
            count += 1
        else:
            break     
    elif key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()