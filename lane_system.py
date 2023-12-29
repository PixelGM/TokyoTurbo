import cv2
import numpy as np

def process_frame(frame):
    # Convert to grayscale for easier processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve edge detection
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny Edge Detector
    edges = cv2.Canny(blur, 50, 150)

    # Define a region of interest (ROI) where to look for lanes
    height, width = frame.shape[:2]
    mask = np.zeros_like(edges)

    # Adjust these points to focus on the road area
    polygon = np.array([[
        (width * 0.1, height),  # Bottom left
        (width * 0.4, height * 0.6),  # Top left
        (width * 0.6, height * 0.6),  # Top right
        (width * 0.9, height)  # Bottom right
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)

    # Use Hough Transform to detect lines
    lines = cv2.HoughLinesP(cropped_edges, 1, np.pi/180, 50, np.array([]), minLineLength=100, maxLineGap=50)

    # Draw lines on the frame
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    return frame

# Load the video
cap = cv2.VideoCapture('video_lane2.mp4')

# Check if video opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Get the frame rate of the video
fps = cap.get(cv2.CAP_PROP_FPS)
frame_delay = int(1000 / fps)  # Delay between frames in milliseconds

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process each frame
    processed_frame = process_frame(frame)

    # Display the processed frame
    cv2.imshow('Lane Detection', processed_frame)

    # Wait for a key event
    key = cv2.waitKey(frame_delay)  # Use frame_delay instead of 1

    # Press 'q' to close the window
    if key & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
