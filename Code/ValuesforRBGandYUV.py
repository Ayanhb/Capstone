import cv2
import numpy as np

# Define the functions RGB2YUV and YUV2RGB
def RGB2YUV(rgb):
    m = np.array([[ 0.29900, -0.16874,  0.50000],
                  [0.58700, -0.33126, -0.41869],
                  [ 0.11400, 0.50000, -0.08131]])
    yuv = np.dot(rgb, m)
    yuv[:,:,1:] += 128.0
    return yuv

def YUV2RGB(yuv):
    m = np.array([[ 1.0, 1.0, 1.0],
                  [-0.000007154783816076815, -0.3441331386566162, 1.7720025777816772],
                  [ 1.4019975662231445, -0.7141380310058594 , 0.00001542569043522235] ])
    rgb = np.dot(yuv, m)
    rgb[:,:,0] -= 179.45477266423404
    rgb[:,:,1] += 135.45870971679688
    rgb[:,:,2] -= 226.8183044444304
    return rgb

# Read the image
image = cv2.imread('your_image.jpg')

# Convert BGR (OpenCV's default) to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert RGB to YUV
image_yuv = RGB2YUV(image_rgb)

# Apply any image processing operations on the YUV image here if needed
# For example, you can modify the Y channel (image_yuv[:, :, 0]) separately

# Convert YUV back to RGB
modified_image_rgb = YUV2RGB(image_yuv)

# Convert RGB back to BGR for OpenCV
modified_image_bgr = cv2.cvtColor(modified_image_rgb.astype(np.uint8), cv2.COLOR_RGB2BGR)

# Display or save the resulting image
cv2.imshow('Modified Image', modified_image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
