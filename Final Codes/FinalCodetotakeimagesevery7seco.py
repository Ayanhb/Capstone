# Code to take images every 7 seconds just JPG 
import time
from datetime import datetime
from picamera2 import Picamera2, Preview

picam2 = Picamera2()

def capture():
    while True:
        timestamp = datetime.now().isoformat()
        picam2.capture_file('//home/ayan/Pictures/JPG/%s.jpg' % timestamp)
        time.sleep(7)

camera_config = picam2.create_still_configuration(main={"size": (4056, 3040)}, lores={"size": (4056, 3040)}, display="lores")
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()

capture()

picam2.stop_preview()

# Combined JPG AND DNG SO THIS CODE
# Final Code to take images every 7 seconds in both JPG and DNG formats
import time
from datetime import datetime
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)

preview_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration(main={"size": (4056, 3040)}, lores={"size": (4056, 3040)}, display="lores", raw={})
picam2.configure(preview_config)

picam2.start()

def capture():
    while True:
        timestamp = datetime.now().isoformat()
        picam2.switch_mode_and_capture_file(capture_config, '//home/ayan/Pictures/JPG/%s.jpg' % timestamp, name="main")
        picam2.switch_mode_and_capture_file(capture_config, '//home/ayan/Pictures/DNG/%s.dng' % timestamp, name="raw")
        time.sleep(7)

capture()

picam2.stop_preview()
