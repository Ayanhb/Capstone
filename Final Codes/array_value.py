#This will showcase some of the matrices 
import cv2
array_value=cv2.imread("raw.dng")
print(array_value)

#This will showcase the Height, width and Channels
import matplotlib.image as img
image=img.imread("raw.dng")
print(image.shape)

#This Code is used for making the DNG file format into a txt format and you can see all the values
from PIL import Image
import numpy as np

im=Image.open("rAw.dng")
data=np.asarray(im, dtype=np.uint8)
np.savetxt("rAwtxt", data.ravel(), fmt='%i')
