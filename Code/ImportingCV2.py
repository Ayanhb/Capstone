from matplotlib import pyplot as plt
import numpy as np 
import time
import cv2

#setup
im = plt.imread('XXX.jpg')
fig, ax=plt.subplots(1,2)
(row, col, channel)= im.shape
im_gray=np.zeros((row, col, 1))

#Grayscale
#R*0.299+G*0.587+B*0.114
start_time=time.time()
im_gray=cv2.cvt.color(im,cv2.COLOR_RGB2GRAY)
end_time=time.time()
elapsed_time=end_time-start_time
print("Elapsed Time is " + str(elapsed_time)+"seconds")

#Display Images
ax[0].imshow(im)
ax[0].axis('off')
ax[0].set_title('RGB')
ax[1].imshow(im_gray, cmap='gray')
ax[1].axis('off')
ax[1].set_title('Grayscale')
plt.show()
