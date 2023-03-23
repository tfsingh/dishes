import os
import face_recognition

# generates encodings for each face in the faces folder
def create_encodings():
    encodings = []
    for file in os.listdir("faces"):
        image = face_recognition.load_image_file("faces/" + file)
        encoding = face_recognition.face_encodings(image)[0]
        encodings.append(encoding)
    return encodings

# generates names for each face in the faces folder
def create_names():
    names = []
    for file in os.listdir("faces"):
        name = file.split(".")[0]
        names.append(name)
    return names

