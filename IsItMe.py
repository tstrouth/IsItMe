import tkinter as tk
from tkinter import filedialog as tkfd
import cv2
import numpy as np
from PIL import ImageTk, Image
import time

#constants
WINDOW_HEIGHT = 700
WINDOW_WIDTH  = 800

#not constants
photo_name_list = ["", "", "", "", ""]
image_reference_list = [None, None, None, None, None]
Bool = None
me = 1

def find_photos(position, button, canvas):
    photo = tkfd.askopenfile()
    file_path = photo.name
    photo_name_list[position] = photo.name
    img = Image.open(file_path).resize((20, 30))
    photo_image = ImageTk.PhotoImage(img)
    image_reference_list[position] = photo_image
    x, y, = button.winfo_x(), button.winfo_y()
    tk.Label(canvas, image=photo_image).place(x=x,y=y-50)

def delete_photos(position, canvas):
    photo_name_list[position] = ""
    canvas.delete(image_reference_list[position])
    image_reference_list[position] = None

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
    print(confidence)
    if ((label == me) and (confidence <= 15)):
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

b1_add = tk.Button(canvas, text="+",
                   height = 2, width = 5,
                   command = lambda: find_photos(0, b1_add, canvas))
canvas.create_window(WINDOW_WIDTH//5, WINDOW_HEIGHT//5, window = b1_add)

b1_minus = tk.Button(canvas, text="-",
                     height = 2, width = 5,
                     command = lambda: delete_photos(0, canvas))
canvas.create_window(WINDOW_WIDTH//5, WINDOW_HEIGHT//5 + 50, window = b1_minus)



b2_add = tk.Button(canvas, text="+",
                   height = 2, width = 5,
                   command = lambda: find_photos(1, b2_add, canvas))
canvas.create_window(WINDOW_WIDTH*.66, WINDOW_HEIGHT//5, window = b2_add)

b2_minus = tk.Button(canvas, text="-",
                     height = 2, width = 5,
                     command = lambda: delete_phots(1, canvas))
canvas.create_window(WINDOW_WIDTH*.66, WINDOW_HEIGHT//5 + 50, window = b2_minus)



b3_add = tk.Button(canvas, text="+",
                   height = 2, width = 5,
                   command = lambda: find_photos(2, b3_add, canvas))
canvas.create_window(WINDOW_WIDTH//2, WINDOW_HEIGHT//5, window = b3_add)
b3_minus = tk.Button(canvas, text="-",
                     height = 2, width = 5,
                     command = lambda: delete_photos(2, canvas))
canvas.create_window(WINDOW_WIDTH//2, WINDOW_HEIGHT//5 + 50, window = b3_minus)



b4_add = tk.Button(canvas, text="+",
                   height = 2, width = 5,
                   command = lambda: find_photos(3, b4_add, canvas))
canvas.create_window(WINDOW_WIDTH//3, WINDOW_HEIGHT//5, window = b4_add)
b4_minus = tk.Button(canvas, text="-",
                     height = 2, width = 5,
                     command = lambda: delete_phots(3, canvas))
canvas.create_window(WINDOW_WIDTH//3, WINDOW_HEIGHT//5 + 50, window = b4_minus)


b5_add = tk.Button(canvas, text="+",
                   height = 2, width = 5,
                   command = lambda: find_photos(4, b5_add, canvas))
canvas.create_window(WINDOW_WIDTH//1.25, WINDOW_HEIGHT//5, window = b5_add)
b5_minus = tk.Button(canvas, text="-",
                     height = 2, width = 5,
                     command = lambda: delete_photos(4, canvas))
canvas.create_window(WINDOW_WIDTH//1.25, WINDOW_HEIGHT//5 + 50,
                     window = b5_minus)




test_button = tk.Button(canvas, text="Click me to add a test photo",
               height = 5, width = 30, command = test_photos)
canvas.create_window(WINDOW_WIDTH//3, WINDOW_HEIGHT//2, window = test_button)

        

window.mainloop()
