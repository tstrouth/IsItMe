import tkinter as tk
from tkinter import filedialog as tkfd
import cv2
import numpy as np

#constants
WINDOW_HEIGHT = 700
WINDOW_WIDTH  = 800

#not constants
photo_name_list = []
Bool = None
me = 1

def find_photos():
    photo = tkfd.askopenfile()
    photo_name_list.append(photo.name)

def detect_face(img):   
    imgUMat = img
    gray = cv2.cvtColor(imgUMat, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    if (len(faces)==0):
        return None, None
    (x, y, w, h) = faces[0]
    return gray[y:y+h,x:x+w], faces[0]

def prepare_training_data():
    faces = []
    labels = []
    for img in photo_name_list: #a collection of file locations as strings
        #print("I am running detect faces")
        image = cv2.imread(img)
        face, rect = detect_face(image)
        if face is not None:
            faces.append(face)
            labels.append(me)
    return faces, labels

def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 2)

def test_photos():
    text = ""
    test_photo = tkfd.askopenfile()
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces, labels = prepare_training_data()
    face_recognizer.train(faces, np.array(labels))
    image = cv2.imread(test_photo.name)
    face, rect = detect_face(image)
    label, confidence = face_recognizer.predict(face)
    if ((label == me) and (confidence <= 20)):
        text = "it's me"
    else:
        text = "it's not me"
    draw_rectangle(image, rect)
    draw_text(image, text, rect[0], rect[1]-5)
    image = cv2.resize(image, (540, 540))
    cv2.imshow("output", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#initiates tkinter window
window = tk.Tk()
#creates the canvas
canvas = tk.Canvas(window, width = WINDOW_WIDTH,
                   height = WINDOW_HEIGHT, bg="green")
canvas.pack()

b1 = tk.Button(canvas, text="Click me to add 5 photos of yourself",
               height = 5, width = 30, command = find_photos)
canvas.create_window(WINDOW_WIDTH//3, WINDOW_HEIGHT//3, window = b1)

b2 = tk.Button(canvas, text="Click me to add a test photo",
               height = 5, width = 30, command = test_photos)
canvas.create_window(WINDOW_WIDTH//3, WINDOW_HEIGHT//2, window = b2)





        

window.mainloop()
