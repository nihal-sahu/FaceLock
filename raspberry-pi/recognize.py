import cv2
import pickle
import serial
import time

#UART communications ports
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.reset_input_buffer()

video = cv2.VideoCapture(0)
video.set(3, 320)
video.set(4, 240)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {} 
with open("labels.pickle", 'rb') as f:
    og_label = pickle.load(f)
    labels = {v:k for k,v in og_label.items()}

print("Beginning video feed...")

while True:
    _, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor = 1.2, minNeighbors = 5)

    for x, y, w, h in faces:
        face_save = gray_frame[y:y+h, x:x+w]
        
        ID, conf = recognizer.predict(face_save)
        if conf >= 20 and conf <= 100:
            cv2.putText(frame, labels[ID], (x-10, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            ser.write(str.encode("Welcome {}!\n".format(labels[ID])));
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)

    cv2.imshow("Video Feed",frame)


    key = cv2.waitKey(1)
    
    if(key == ord('q')):
        print("Exiting...")
        break



video.release()
cv2.destroyAllWindows()
print("Exited.")
