import face_recognition
import cv2
import update
import detection
import time

# defines variables for taking in video from webcams
video_capture = cv2.VideoCapture(1)
object_capture = cv2.VideoCapture(0)

# stores the previous (relevant) dish frames
obj_frames = [object_capture.read()[1]]

# time to wait before checking if a dish has been added
wait_time = 10

# defines the resting similarity score
similarity_score = detection.newSimilarity(obj_frames[-1], object_capture)

while True:
    # takes a new image from each webcam
    ret, face_frame = video_capture.read()
    ob, obj_frame = object_capture.read()

    face_names = []

    detection.match_faces(face_names, face_frame)

    # displays the video frames
    cv2.imshow('Video', face_frame)    
    cv2.imshow('Object', obj_frame)
    
    # if a face is detected, check if the dish has changed
    if (detection.dish(face_names, obj_frame, obj_frames[-1], similarity_score)):

        time.sleep(wait_time)

        # if there is still a dish after the designated wait time, update the backend and send a message
        if detection.checkDiff(object_capture.read()[1], obj_frames[-1], similarity_score):

            update.send_message(face_names)
            update.update_backend(face_names)

            # update the previous dish frames
            obj_frames.append(object_capture.read()[1])
            similarity_score = detection.newSimilarity(obj_frames[-1], object_capture)

    # quits on q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()