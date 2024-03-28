#This will showcase some of the matrices 
#import cv2
#array_value=cv2.imread("raw.dng")
#print(array_value)

#This will showcase the Height, width and Channels
#import matplotlib.image as img
#image=img.imread("raw.dng")
#print(image.shape)

#This Code is used for making the DNG file format into a txt format and you can see all the values
#from PIL import Image
#import numpy as np

#im=Image.open("rAw.dng")
#data=np.asarray(im, dtype=np.uint8)
#np.savetxt("rAwtxt", data.ravel(), fmt='%i')

#Code for capturing the DNG and JPG Files
import time

from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)

preview_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration(raw={})
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

picam2.switch_mode_and_capture_file(capture_config, "full.dng", name="raw")


