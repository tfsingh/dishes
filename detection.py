import numpy as np
import cv2
import face_recognition
import generate_encodings
from skimage.metrics import structural_similarity

# gets encodings and names from generate_encodings.py
known_face_encodings = generate_encodings.create_encodings()
known_face_names = generate_encodings.create_names()

# gets the similarity score of two frames
def getScore(frame_1, frame_2):
    before_gray = cv2.cvtColor(frame_1, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)
    score, _ = structural_similarity(before_gray, after_gray, full=True)
    return score * 100

# returns true if two dish frames are significantly different
def checkDiff(frame_1, frame_2, image_similarity):
    score = getScore(frame_1, frame_2)
    return np.abs(score - image_similarity) > 5

# returns true if a face is detected and the dish has changed
def dish(face_names, obj_frame, prev_frame, similarity_score):
    return face_names and checkDiff(obj_frame, prev_frame, similarity_score)

# generates a new similarity score for the current dish frame
def newSimilarity(prev_frame, object_capture):
    for i in range(10):
        object_capture.read()[1]
    return getScore(prev_frame, object_capture.read()[1])
    
# draws boxes around faces and labels them
def draw_boxes(face_locations, face_names, face_frame):
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(face_frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(face_frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

        font = cv2.FONT_HERSHEY_DUPLEX
        
        cv2.putText(face_frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)   

# matches faces to known faces
def match_faces(face_names, face_frame):
    small_frame = cv2.resize(face_frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "unknown"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    #draw_boxes(face_locations, face_names, faceFrame)
  