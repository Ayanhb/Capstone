# Code including Location
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
import geocoder

#v0.01

# setup
framerate  = 1
cap_length = 7000  # in mS (7 seconds)

# setup directories to save to...
Home_Files  = []
Home_Files.append(os.getlogin())
jpg_dir = "/home/" + Home_Files[0]+ "/Pictures/JPG/"
dng_dir = "/home/" + Home_Files[0]+ "/Pictures/DNG/"

# create directories if they don't exist
if not os.path.exists(jpg_dir):
    os.makedirs(jpg_dir)
if not os.path.exists(dng_dir):
    os.makedirs(dng_dir)

# get camera location using geocoder
g = geocoder.ip('me')
camera_location = g.latlng

# start camera with Picamera2
print("Starting Camera...")
picamera2 = Picamera2()
picamera2.start_preview(Preview.QTGL)

# configure camera settings
picamera2.configure(picamera2.create_still_configuration(main={"format": 'JPEG', "size": (4056, 3040)},
                                                          raw={"format": 'RAW10', "size": (4056, 3040)}))

# capture loop
while True:
    # capture JPG and DNG
    jpg_file = jpg_dir + datetime.datetime.now().strftime("%y%m%d%H%M%S") + ".jpg"
    dng_file = dng_dir + datetime.datetime.now().strftime("%y%m%d%H%M%S") + ".dng"
    picamera2.capture_file(jpg_file, format='JPEG')
    picamera2.capture_file(dng_file, format='RAW10')

    # add camera location to file names
    jpg_file_with_location = jpg_file + "_" + str(camera_location[0]) + "_" + str(camera_location[1]) + ".jpg"
    dng_file_with_location = dng_file + "_" + str(camera_location[0]) + "_" + str(camera_location[1]) + ".dng"

    # rename files with location
    os.rename(jpg_file, jpg_file_with_location)
    os.rename(dng_file, dng_file_with_location)

    print("Saved: ", jpg_file_with_location, "and", dng_file_with_location)

    # wait for 7 seconds
    time.sleep(7)

    # stop camera preview
    #picamera2.stop_preview()

    # wait for a key press
    print( "Press a key to exit")
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()
    sys.exit()

# stop camera preview
picamera2.stop_preview()