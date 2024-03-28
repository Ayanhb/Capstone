import cv2
im=cv2.imread('full.jpg')
gray=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
print(gray)