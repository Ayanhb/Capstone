#Test Output
import cv2
im=cv2.imread('computer.jpg',0)
for i in range(im.height):
    for j in range(im.width):
        print(im[i,j])
print("\n",i)
