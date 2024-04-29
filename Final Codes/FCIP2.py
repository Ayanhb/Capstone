import time
import os
import logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from picamera2 import Picamera2, Preview
import subprocess

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s\t%(levelname)s\tTemperature: %(temperature)s\tMain Image Size: %(main_image_size)s MB\tRaw Image Size: %(raw_image_size)s MB\t%(message)s')
logname = "/home/ayan/Pictures/Log/Telemetry.log"
handler = TimedRotatingFileHandler(logname, when="m", interval=10)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

os.environ['LIBCAMERA_LOG_LEVELS'] = '4'
Picamera2.set_logging(Picamera2.ERROR)
picam2 = Picamera2()  # fix the typo

capture_config = picam2.create_still_configuration(main={"size": (4056, 3040)}, lores={"size": (4056, 3040)}, display="lores", raw={})

picam2.start()

def get_temperature():
    # Get the temperature of the Raspberry Pi
    temp_output = subprocess.check_output(["vcgencmd", "measure_temp"])
    temp = temp_output.decode("utf-8").split("=")[1].strip("'\n°C")
    return float(temp)

def capture():
    while True:
        timestamp = datetime.now().isoformat()
        temperature = get_temperature()
        logger.info("", extra={"temperature": temperature, "main_image_size": 0, "raw_image_size": 0})

        jpg_file_path = f'/home/ayan/Pictures/JPG/{timestamp}.jpg'
        dng_file_path = f'/home/ayan/Pictures/DNG/{timestamp}.dng'

        picam2.switch_mode_and_capture_file(capture_config, jpg_file_path, name="main")
        jpg_size = os.path.getsize(jpg_file_path) / 1024 / 1024  # in MB
        logger.info("", extra={"main_image_size": jpg_size})

        picam2.switch_mode_and_capture_file(capture_config, dng_file_path, name="raw")
        dng_size = os.path.getsize(dng_file_path) / 1024 / 1024  # in MB
        logger.info("", extra={"raw_image_size": dng_size})

        time.sleep(4)

capture()
