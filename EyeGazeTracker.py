# Import Libraries
import cv2

# Import XML Pre-Trained Haar Cascade Classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Define Blob Detector Parameters
detector_params = cv2.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1000 # Reduce this value for person sitting further away from camera
detector = cv2.SimpleBlobDetector_create(detector_params)

# Blob Detection Function Within Detected Eye
def blob_process(img, threshold, detector):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow('pupil', img)
    img = cv2.erode(img, None, iterations=2)
    img = cv2.dilate(img, None, iterations=4)
    img = cv2.medianBlur(img, 5)
    keypoints = detector.detect(img)
    return keypoints

# Pass Function for Tracker Bar
def nothing(x):
    pass

# Capture Video and Create Track Bar
cap = cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.createTrackbar('threshold', 'image', 0, 255, nothing)

# Initiate Face, Eye, and Pupil Detection
while True:
    ret, img = cap.read()
    gray_picture = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converts frames into grayscale
    faces = face_cascade.detectMultiScale(gray_picture, 1.3, 5) # Gets face boundary in image frame(x=x-cord,y=y-cord,w=width,h=height)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) # Draws boundary on the detected face
        cv2.putText(img, 'Face', (x, y-10), cv2.FONT_HERSHEY_PLAIN, 0.9, (0, 255, 0), 2) # Display text
        gray_face = gray_picture[y:y + int(h / 2), x:x + w] # Upper half of face to avoid false detection on chin,nose, mouth, etc.
        face_image = img[y:y + h, x:x + w] # Separating face from the background
        eyes = eye_cascade.detectMultiScale(gray_face) # Obtains all detected eye boxes in (x,y,w,h) array
        counter = 0;
        for eye in eyes:
            # threshold = 100
            eye_image = None
            threshold = cv2.getTrackbarPos('threshold', 'image') # Obtains threshold value from the track bar in the UI
            eye_image = img[faces[0][1]+eye[1]+15 : faces[0][1]+eye[1]+eye[3]-10, faces[0][0]+eye[0]+10 : faces[0][0]+eye[0]+eye[2]-10] # Shortening the eye box to avoid eye lashes, eye brows, etc.
            if eye_image.size ==0: # The code runs into error if empty image is passed into blob detector, to avoid that we use this if-else statement
                break
            else:
                keypoints = blob_process(eye_image, threshold, detector)
                counter = counter + 1
                for keyPoint in keypoints: # Obtains keypoints in readable format
                    x = keyPoint.pt[0]
                    y = keyPoint.pt[1]
                    s = keyPoint.size
                    print(f"For Eye {counter}; Pupil: X-Cord = {x:.2f}, Y-Cord = {y:.2f}, Radius = {s:.2f}") # Outputs the detected pupil's X-Coordinates, Y-Coordinates and Radius
                eye_image = cv2.drawKeypoints(eye_image, keypoints, eye_image, (255, 255, 255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                cv2.rectangle(face_image, (eye[0], eye[1]), (eye[0] + eye[2], eye[1] + eye[3]), (255, 0, 0), 2) # Draws eye box
                cv2.putText(face_image, 'Eyes', (eye[0], eye[1]-10), cv2.FONT_HERSHEY_PLAIN, 0.9, (255, 0, 0), 2) # Displays text
    cv2.imshow('image', img)
    key=cv2.waitKey(100) # Parameter is in milliseconds
    if key==27: # Press escape to exit
        break
cv2.destroyAllWindows()