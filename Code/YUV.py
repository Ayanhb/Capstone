from picamera2 import Picamera2

picam2 = Picamera2()

main = {'size': (1640, 1232), 'format': 'RGB888'}  # or BGR888
lores = {'size': (640, 480), 'format': 'YUV420'}  # on a Pi 5 you have RGB888 here (not on earlier Pis)
raw = {'size': (1640, 1232), 'format': 'SRGGB8'}  # this will select the full FoV 80fps mode
controls = {'FrameRate': 80}  # will default to 30fps otherwise
config = picam2.create_video_configuration(main, lores=lores, raw=raw, controls=controls)
picam2.configure(config)
picam2.start()

while True:
    request = picam2.capture_request()

    # If you want to use the YUV image for something:
    yuv = request.make_array('lores')

    # If you want to save the RGB image:
    request.save('main', "file.jpg")  # or rgb = request.make_array('main') just to grab it

    # Must always release the request.
    request.release()