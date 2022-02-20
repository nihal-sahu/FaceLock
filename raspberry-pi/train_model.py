# import the required libraries
import cv2
import os
import numpy as np
from PIL import Image
import pickle


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
trainer = cv2.face.LBPHFaceRecognizer_create()

def getdata():

    current_id = 0
    label_id = {} 
    face_train = [] 
    face_label = [] 
    
    #finding base directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(BASE_DIR,'dataset')

    for root, dirs, files in os.walk(img_dir):
        for file in files:
            path = os.path.join(root, file)
            label = os.path.basename(root)
                
            # providing a unique ID if we are training for more than one face
            if not label in label_id:
                label_id[label] = current_id
                current_id += 1
            ID = label_id[label]

            pil_image = Image.open(path).convert("L")
            img_list = np.array(pil_image, "uint8")
        
            faces = face_cascade.detectMultiScale(img_list)

            for x, y, w, h in faces:
                img = img_list[y:y+h, x:x+w]
                cv2.imshow("Training",img)
                cv2.waitKey(1)
                face_train.append(img)
                face_label.append(ID)

    # getting all labels data into one file
    with open("labels.pickle", 'wb') as f:
        pickle.dump(label_id, f)
   

    return face_train, face_label




#creating the training yml data
face,ids = getdata()
trainer.train(face, np.array(ids))
trainer.save("trainer.yml")
