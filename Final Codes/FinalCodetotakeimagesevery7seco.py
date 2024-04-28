#Final Code for Image System on Flight 
import time 
import os 
import logging 
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from picamera2 import Picamera2, Preview 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t%(message)s')
logname = "/home/ayan/Pictures/Log/Telemetry.log"
handler = TimedRotatingFileHandler(logname, when="m", interval=10)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

os.environ['LIBCAMERA_LOG_LEVELS'] = '4'
Picamera2.set_logging(Picamera2.ERROR)
picam2 - Picamera2()

capture_config = picam2.create_still_configuration(main={"size": (4056, 3040)}, lores={"size": (4056, 3040)}, display="lores", raw={})

picam2.start()

def capture():
    while True:
        timestamp = datetime.now().isoformat()
        picam2.switch_mode_and_capture_file(capture_config, '//home/ayan/Pictures/JPG/%s.jpg' % timestamp, name="main")
        picam2.switch_mode_and_capture_file(capture_config, '//home/ayan/Pictures/DNG/%s.dng' % timestamp, name="raw")
        time.sleep(4)

capture()
