import cv2
img=cv2.imread('computer.jpg',0)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        print(img[i][j])


