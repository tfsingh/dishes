import face_recognition
import cv2
import update
import face

video_capture = cv2.VideoCapture(1)
object_capture = cv2.VideoCapture(0)

objFrames = [object_capture.read()[1]]

def dish(face_names, objFrame):

    # if face names is not empty
        # check if current object frame is different that previous
        # if it is, wait 120 seconds
        # if object frame is still different, then trigger a text that blames all face names for leaving a dish in the sink
    if face_names:
        print(cv2.absdiff(objFrame, objFrames[-1]).sum())
        return True
    
    return False

    

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, faceFrame = video_capture.read()
    ob, objFrame = object_capture.read()

    face_names = []

    
    face.match_faces(face_encodings, face_locations, face_names, faceFrame)

    cv2.imshow('Video', faceFrame)    
    cv2.imshow('Object', objFrame)
    if (dish(face_names, objFrame)):
        # push notification to twilio
        update.send_message(face_names)

        # update backend
        update.update_backend(face_names)

        break
    
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break






# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()