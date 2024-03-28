### I use this script to take RGB and near-IR images in rapid succession by modulating the
### IR filter in the camera using GPIO control.

### Import libraries
import RPi.GPIO as GPIO
import time
from picamera2 import Picamera2
import numpy as np
from matplotlib import pyplot as plt

# Configure camera
picam2 = Picamera2()

### Initial GPIO setup
GPIO.setmode(GPIO.BCM) # use GPIO numbering
GPIO.setup(23, GPIO.OUT) # set GPIO23 as an output

### Take IR image in YUV format
capture_config = picam2.create_still_configuration(main = {"size": (4056, 3040), "format": "YUV420"})
#capture_config = picam2.create_still_configuration()
picam2.configure(capture_config)
picam2.start()
GPIO.output(23, 0)
time.sleep(2)
arr_ir = picam2.capture_array("main")
picam2.stop()

### Take RGB image
capture_config = picam2.create_still_configuration()
picam2.configure(capture_config)
picam2.start()
GPIO.output(23, 1)
time.sleep(2)
arr_rgb = picam2.capture_array("main")
picam2.stop()

### Clear GPIO
GPIO.cleanup()

### Plot the images
f, ax = plt.subplots(1,2)
ax[0].imshow(arr_rgb)
ax[0].set_title('RGB')
ax[1].imshow(arr_ir)
ax[1].set_title('No IR')
plt.show()