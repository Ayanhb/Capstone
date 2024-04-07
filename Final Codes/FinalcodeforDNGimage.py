#!/usr/bin/env python3
import time
import os, subprocess
import signal
import datetime
import glob
import sys
import cv2
import numpy as np
from picamera2 import Picamera2, Preview

#v0.01

# setup
framerate  = 10    # fps
cap_length = 5000  # in mS

# setup directory to save to...
Home_Files  = []
Home_Files.append(os.getlogin())
pic_dir = "/home/" + Home_Files[0]+ "/Pictures/"

# clear ram
print("Clearing RAM...")
frames = glob.glob('/run/shm/*.raw')
for tt in range(0,len(frames)):
    os.remove(frames[tt])

# start camera with Picamera2
print("Starting Camera...")
picamera2 = Picamera2()
picamera2.start_preview(Preview.QTGL)

# capture for cap_length
start = time.monotonic()
while time.monotonic() - start < cap_length/1000:
    time.sleep(0.1)

# stop camera preview
picamera2.stop_preview()

# capture DNG
picamera2.capture_file(pic_dir + "capture.dng")

print("Saved: ", pic_dir + "capture.dng")

# wait for a key press
print( "Press a key to exit")
k = cv2.waitKey(0)
cv2.destroyAllWindows()
sys.exit()