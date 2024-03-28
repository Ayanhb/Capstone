#GetGrayscaleandPixelwillbeanumberrepresnetingtheIntensityofWhite
import cv2
img=cv2.imread('computer.jpg',0)
print("image Shape = ", img.shape)
print("Image Array = ", img)
print("Pixel at index (5,5): ", img[5][5])
