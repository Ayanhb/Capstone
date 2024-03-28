from picamera2 import Picamera2, Preview
import time
import os

# Create a folder to save images if it doesn't exist
save_folder = "raw_images"
os.makedirs(save_folder, exist_ok=True)

picam = Picamera2()

camera_config = picam.create_still_configuration(
    main={"size": (1920, 1080)},
    lores={"size": (640, 480)},
    display="lores",
)

picam.start_preview(Preview.QTGL)
picam.start()

try:
    for i in range(5):  # Capture 5 images
        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = os.path.join(save_folder, f"image_{timestamp}.raw")
        
        picam.capture_file(filename)
        print(f"Captured image: {filename}")

        time.sleep(1)  # Wait for a second between captures

finally:
    picam.stop()  # Stop the camera when done
