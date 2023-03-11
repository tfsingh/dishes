import numpy as np
import cv2
import face_recognition
import generate_encodings
from skimage.metrics import structural_similarity


known_face_encodings = generate_encodings.create_encodings()
known_face_names = generate_encodings.create_names()

def getScore(frame1, frame2):
    before_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    (score, diff) = structural_similarity(before_gray, after_gray, full=True)
    return score * 100

def checkDiff(frame1, frame2, image_similarity):
    before_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Compute SSIM between the two images
    (score, diff) = structural_similarity(before_gray, after_gray, full=True)
    print("Image Similarity: {:.4f}%".format(score * 100))
    return np.abs(score*100 - image_similarity) > 5

def dish(face_names, objFrame, prevFrame, similarity_score):
    
    #if there is a face in the frame and there is a significant difference between the current frame and the previous frame, then return true.
    return face_names and checkDiff(objFrame, prevFrame, similarity_score)
    

def draw_boxes(face_locations, face_names, faceFrame):
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(faceFrame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(faceFrame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

        font = cv2.FONT_HERSHEY_DUPLEX
        
        cv2.putText(faceFrame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)   

def match_faces(face_encodings, face_locations, face_names, faceFrame):
    small_frame = cv2.resize(faceFrame, (0, 0), fx=0.25, fy=0.25)
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
  