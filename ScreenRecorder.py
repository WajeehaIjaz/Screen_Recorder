import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

# Get the screen dimensions (width and height in pixels)
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# Store dimensions as a tuple for video writer
dim = (width, height)

# SET the codec for video compression (XVID format)
f = cv2.VideoWriter_fourcc(*"XVID")

# Initialize the video writer object
# Parameters: output filename, codec, frame rate (10 fps), frame dimensions
output = cv2.VideoWriter("test.mp4", f, 10.0, dim)

# Record the start time
start_time = time.time()

# Set recording duration to 10 seconds
dur = 10
end_time = start_time + dur

# Main recording loop
while True:
    # Capture screenshot of the entire screen
    image = pyautogui.screenshot()
    
    # Convert PIL Image to numpy array
    frame_1 = np.array(image)
    
    # Convert color from BGR to RGB (OpenCV uses BGR, PIL uses RGB)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    
    # Write the frame to the video file
    output.write(frame)
    
    # Break loop if duration exceeded(current_time>end_time)
    if time.time() > end_time:
        break

# Release the video writer to save the file properly
output.release()
print("---END---")