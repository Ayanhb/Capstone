
import time

from picamera2 import Picamera2, Preview

picam=Picamera2

def main():
    picam = setup_camera_grey()
while True:
    #Hot looped measured
    img = picam.capture_array()
    img_preproc = cv2.cvtColor(img, cv2.COLOR_BGR2GREY)
    #end
    
def setup_camera():
    picam = Picamera2()
    config = picam.create_preview_configuration()
    config['main']['size'] = IMG_DIMS
    config['main']['format'] = "RGB888"
    picam.align_configuration(config)
    print(config)
    picam.configure(config)
    picam.start()
    
    return picam
