import os
import cv2
import numpy as np

from PIL import Image 

names = []
paths = []

#contain all our users into one array
for users in os.listdir("dataset"):
    names.append(users)

#contain all our images in one array
for name in names:
    for frame in os.listdir("dataset/{}".format(name)):
        path_string = os.path.join("dataset/{}".format(name), frame)
        paths.append(path_string)

faces= []
ids = []

#contain image into a numpy array
for img_path in paths:
    image = Image.open(img_path).convert("L")

    imgNp = np.array(image, "uint8")
    faces.append(imgNp)
    #containing ids in numpy array
    id = int(img_path.split("/")[2].split("_")[0])
    ids.append(id)

ids = np.array(ids)

trainer = cv2.face.LBPHFaceRecognizer_create()

trainer.train(faces, ids)
trainer.write("trainer.yml")

