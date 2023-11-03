import cv2
import numpy as np

def callback(x):
    pass

# Initialize camera
cap = cv2.VideoCapture(0)

# Create a window with a slider for adjusting the sensitivity
cv2.namedWindow('Controls')
cv2.createTrackbar('Sensitivity', 'Controls', 0, 255, callback)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the slider value for adjusting the sensitivity
    sensitivity = cv2.getTrackbarPos('Sensitivity', 'Controls')

    # Define the range for red color
    lower_red = np.array([0, 120 - sensitivity, 70 - sensitivity])
    upper_red = np.array([10, 255, 255])

    # Create a mask for red color
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour and its center
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0

        # Mark the center on the original frame
        cv2.circle(frame, (cX, cY), 5, (0, 255, 0), 2)

    # Display the marked frame
    cv2.imshow('Red Color', frame)

    # Wait for a key event for 1 millisecond
    key = cv2.waitKey(1)

    # Press 'q' to close the window
    if key & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
