from picamera2 import Picamera2
import numpy as np
import cv2

# Initialize the PiCamera
picam2 = Picamera2()
WIDTH = 1024
HEIGHT = 768
config = picam2.create_preview_configuration({'format': 'YUV420', 'size': (WIDTH, HEIGHT)})
picam2.configure(config)
picam2.start()

# Create a numpy array to hold image data
yuv_array = np.empty((HEIGHT * 3 // 2, WIDTH), dtype=np.uint8)

# Capture a single frame
picam2.capture(yuv_array, format='YUV420')

# Convert RGB to grayscale
grey = cv2.cvtColor(yuv_array, cv2.COLOR_YUV2GRAY_420)

# Save the grayscale image using OpenCV
cv2.imwrite("grayscale_image.jpg", grey)

# Stop the camera preview
picam2.stop()


