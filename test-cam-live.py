import cv2

# Replace 0 with the index of your camera if you have multiple cameras
cap = cv2.VideoCapture(0)

while True:
  # Capture frame-by-frame
  ret, frame = cap.read()

  # Display the resulting frame
  cv2.imshow('Webcam Feed', frame)

  # Exit if 'q' key is pressed
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()