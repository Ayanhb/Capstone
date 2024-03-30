#Albedo Code 

# Specify the name of the image file 
filename = ''

# Import the Libraries 
import numpy as np 
import matplotlib.pyplot as plt 
from skimage import io # sudo apt-get install python-skimage

# Load & Show the Image 
img = io.imread(filename)
plt.figure()
plt.imshow(img, cmpa='gray')

# Get the dimensions of the image 
ny,nx,nz = np.shape(img); print('ny,nx = ', ny, nx)
midptx = int(nx/2) # middle position (Horizontal)
midpty = int(ny/2) # middle position (Vertical)

# Convert the image to grayscale for albedo analysis 
img = io.imread(filename, as_gray=True)

# Extract & Plot a Horizontal Slice 
plt.figure()
plt.plot(np.array(img[midpty,:]))
plt.grid(True)
plt.title('Left-Right Horizontal Slice Through the Middle of The Image')

# Computing the albedo (Can be done with a calculator as well)
#albedo = (.45-.05)/(.6-.05) # Here you use the plot to determine the values you want to compare and then the second part is the whole range 
#print(albedo)