# import cv2
#
# # Try a few common camera indexes
# for i in range(10):  # Change the range based on your expectation
#   cap = cv2.VideoCapture(i)
#   if cap.isOpened():
#       print(f"Camera found at index {i}")
#       # You can break here if you only want the first camera
#       # cap.release()  # Release the capture if not using it further
#       break
#   else:
#       print(f"No camera found at index {i}")

# cap.release()  # Release the capture if not closed before


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