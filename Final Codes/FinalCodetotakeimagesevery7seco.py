# Final Code to take images every 7 seconds 
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


import time
import numpy as np
from datetime import datetime
from picamera2 import Picamera2, Preview

picam2 = Picamera2()

def capture():
    while True:
        timestamp = datetime.now().isoformat()
        picam2.capture_file('//home/ayan/Pictures/JPG/%s.jpg' % timestamp)
        with picam2.capture_stream('dng') as stream:
            picam2.capture(stream, 'dng')
            array = np.frombuffer(stream.getvalue(), dtype=np.uint16)
            array = array.reshape((4056, 3040))
            with open('//home/ayan/Pictures/DNG/%s.dng' % timestamp, 'wb') as f:
                f.write(stream.getvalue())
        time.sleep(7)

camera_config = picam2.create_still_configuration(main={"size": (4056, 3040)}, lores={"size": (4056, 3040)}, display="lores")
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()

capture()

picam2.stop_preview()
