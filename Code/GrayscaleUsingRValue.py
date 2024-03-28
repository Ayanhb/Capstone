import cv2
i=cv2.imread('computer.jpg', cv2.IMREAD_COLOR)
i.shape
r=i[:,:,2]
r.shape
cv2.imwrite('computer.jpg',r)
