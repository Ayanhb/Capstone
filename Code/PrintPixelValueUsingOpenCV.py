#Print Pixel Value Using OpenCV
import cv2
im= cv2.imread('computer.jpg')
gray=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
print(gray)
