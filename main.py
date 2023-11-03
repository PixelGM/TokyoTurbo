import cv2
import numpy as np

# Initialize camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find the location of the minimum pixel value in the grayscale frame
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

    # Mark the location of the minimum pixel value on the original frame
    cv2.circle(frame, maxLoc, 5, (0, 255, 0), 2)

    # Display the marked frame
    cv2.imshow('Whitest Point', frame)

    # Wait for a key event for 1 millisecond
    key = cv2.waitKey(1)

    # Press 'q' to close the window
    if key & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
