import cv2
import face_recognition
import os

# Load known faces from the "known_faces" directory
known_faces = []
known_names = []
known_faces_dir = "known_faces"

for filename in os.listdir(known_faces_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load image and encode face
        img = face_recognition.load_image_file(f"{known_faces_dir}/{filename}")
        encoding = face_recognition.face_encodings(img)[0]
        known_faces.append(encoding)
        # Store name without file extension
        known_names.append(os.path.splitext(filename)[0])

# Initialize camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect and encode faces in the current frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        if True in matches:
            # Use the name of the first matched known face
            match_index = matches.index(True)
            name = known_names[match_index]

        # Scale back up face location since the frame was resized
        top, right, bottom, left = [v * 4 for v in face_location]

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Display name if known, otherwise display "Unknown"
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Webcam Feed", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
