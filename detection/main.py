import face_recognition
import cv2
import update
import func
import time

video_capture = cv2.VideoCapture(1)
object_capture = cv2.VideoCapture(0)


time.sleep(1)
objFrames = [object_capture.read()[1]]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

def newSimilarity():
    for i in range(10):
        object_capture.read()[1]
    return func.getScore(objFrames[-1], object_capture.read()[1])


similarity_score = newSimilarity()
#print("similarity", similarity_score)
while True:
    ret, faceFrame = video_capture.read()
    ob, objFrame = object_capture.read()

    face_names = []

    
    func.match_faces(face_encodings, face_locations, face_names, faceFrame)

    cv2.imshow('Video', faceFrame)    
    cv2.imshow('Object', objFrame)
    
    if (func.dish(face_names, objFrame, objFrames[-1], similarity_score)):
        print("here")

        time.sleep(10)

        if func.checkDiff(object_capture.read()[1], objFrames[-1], similarity_score):
        # push notification to twilio
            update.send_message(face_names)

        # update backend
        #update.update_backend(face_names)
            print(face_names[0] + " left a dish in the sink")
            
            objFrames.append(object_capture.read()[1])
            similarity_score = newSimilarity()
            print("similarity", similarity_score)

        print("done")

    
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break






# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()