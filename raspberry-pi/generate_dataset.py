import cv2
from pathlib import Path

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

#downscale video resolution to ensure smooth fps on pi
video.set(3, 320)
video.set(4, 240)

print("Enter the name of the person: ")
userName = input()

print("\nPress 'q' to exit, press 's' to save an image to the dataset.\nScript terminates after 20 images.\nMAKE SURE THERE IS A GREEN SQUARE AROUND YOUR FACE BEFORE CAPTURING AN IMAGE.\nCapture begun.")

count = 1 #used to see how many images we have saved

#method to save images
def saveImage(frame, userName, imgId):
    Path("dataset/{}".format(userName)).mkdir(parents=True, exist_ok = True)       #create folder to save images
    cv2.imwrite("dataset/{}/{}_{}.jpg".format(userName, userName, imgId), frame)

while True:

    _, frame = video.read()
    originalFrame = frame

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
    #save only 20 images
        if count < 20:
            cropped = originalFrame[coords[1]:coords[1] + coords[3], coords[0]:coords[0] + coords[2]]
            saveImage(cropped, userName, count)
            print("{}/20 images saved".format(count))
            count += 1
        else:
            print("Capture completed.")
            break    

    faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 5)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
        coords = [x, y, w, h]

    cv2.imshow("Capturing", frame)

    if key == ord('q'):
        print("Exiting...")
        break

video.release()
cv2.destroyAllWindows()
print("Exited successfully.")