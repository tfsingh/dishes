import os
import face_recognition

#create an image and an encoding for each file in the faces folder
def create_encodings():
    encodings = []
    for file in os.listdir("faces"):
        image = face_recognition.load_image_file("faces/" + file)
        encoding = face_recognition.face_encodings(image)[0]
        encodings.append(encoding)

#return an array of names of people in the faces folder
def create_names():
    names = []
    for file in os.listdir("faces"):
        name = file.split(".")[0]
        names.append(name)
    return names

