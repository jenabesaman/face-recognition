import cv2
import dlib

def videoFaceDet(video_file_path):
    # Initialize video capture
    video = cv2.VideoCapture(video_file_path)

    # Check if the video file opened successfully
    if not video.isOpened():
        print(f"Error: Could not open video file {video_file_path}")
        return

    # Initialize dlib's face detector
    face_detector = dlib.get_frontal_face_detector()

    # Continuously process video frames
    while True:
        # Read a frame from the video
        check, frame = video.read()

        # Break the loop if no frame is returned (end of video)
        if not check:
            print("End of video or error reading frame.")
            break

        # Reduce frame size for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # Convert the frame to grayscale
        grayImg = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)

        # Detect faces using dlib
        faces = face_detector(grayImg)

        # Draw rectangles around detected faces
        for face in faces:
            x, y, w, h = (face.left(), face.top(), face.width(), face.height())
            x, y, w, h = int(x * 2), int(y * 2), int(w * 2), int(h * 2)  # Scale back to original size
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the processed frame
        cv2.imshow("Face Detection", frame)

        # Exit the loop when 'q' is pressed
        key = cv2.waitKey(1)
        if key == ord('q'):
            print("Exiting on user request.")
            break

    # Close all OpenCV windows
    cv2.destroyAllWindows()

    # Release the video capture object
    video.release()

# Specify the path to your video file
video_file_path = "KDT.mp4"

# Start face detection on the video file
videoFaceDet(video_file_path)