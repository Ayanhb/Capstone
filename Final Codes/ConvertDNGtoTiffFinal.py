#!/usr/bin/env python3
import time
import os, subprocess
import signal
import datetime
import glob
import sys
import cv2
import numpy as np

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
   
# start camera with subprocess
print("Starting Camera...")
command = "rpicam-raw -n -t 0 --mode 4056:3040:10:U --width 4056 --height 3040 --segment 1 --framerate " + str(framerate) + " -o /run/shm/temp_%06d.raw"
s = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)
poll = s.poll()
while poll != None:
    print("waiting...")
    poll = s.poll()
     
# capture for cap_length
start = time.monotonic()
while time.monotonic() - start < cap_length/1000:
    time.sleep(0.1)
        
# stop camera subprocess
os.killpg(s.pid, signal.SIGTERM)
       
# open frame
frames = glob.glob('/run/shm/temp*.raw')
fd = open(frames[0], 'rb')
f = np.fromfile (fd,dtype=np.uint16,count=-1)
im = f.reshape((3040,4064))
im = im * 16 # remove this line if using a Pi5
fd.close()

# save TIF
fname = frames[0].split('.')
now = datetime.datetime.now()
timestamp = now.strftime("%y%m%d%H%M%S")
cv2.imwrite(pic_dir + timestamp + ".tif", im)
print("Saved: " , pic_dir + timestamp + ".tif")
result = cv2.resize(im, dsize=(int(4064/4),int(3040/4)), interpolation=cv2.INTER_CUBIC)
cv2.imshow(frames[0],result)

# wait for a key press
print( "Press a key to exit")
k = cv2.waitKey(0)
cv2.destroyAllWindows()
sys.exit()