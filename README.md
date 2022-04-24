# FaceLock

## Second place overall winner of Cuse Hacks 2022, and best use of GitHub Award. 
Check out the devpost submission here: https://devpost.com/software/facelock-hezv8n

![IMG_3179](https://user-images.githubusercontent.com/87585163/164988756-62529d25-b3c6-4906-91f2-c859b4a6daf2.jpg)

## About the Project:
FaceLock is a facial recognition locking system built with an Arduino and Raspberry Pi communicating together over UART.
There are scripts to train and create models from the basic webcam output. The camera scans for familiar faces, and when they are detected, a signal is sent over UART to a servo motor in order to unlock the door. 

## Setup: 
### Step 1: 
Run identify.py on your system to make sure that you have the required libraries (OpenCV). You should see a square appear around your face on the video feed. 
### Step 2: 
Run generate_dataset.py to collect images of your face. The instructions will be outputted in the terminal. Try to capture different angles of your face, and make sure a green square is appearing around your face when trying to capture an image. 
### Step 3: 
Run train_model.py to create a model from the collected images.
### Step 4: 
Flash the lcdAndMotor code to your Arduino.
### Step 5: 
Connect your Arduino and Pi (or other computer system) and run recognize.py. Leave it running with your webcam in a great spot with good lighting. This controls the unlocking/locking. The door will automatically lock after a set amount of time. 

Enjoy :)


