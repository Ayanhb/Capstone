# Import opencv library
import cv2 as cv

# Load the image into a variable using the imread function.
img = cv.imread("ASU.jpeg")

# Converting the image from BGR to RGB since OpenCV generally uses BGR image format.
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Now converting the image from RGB to YUV
img_yuv = cv.cvtColor(img_rgb, cv.COLOR_RGB2YUV)

# Showing all the images
cv.imshow("RGB Image", img_rgb)
cv.imshow("YUV Image", img_yuv)
cv.imshow("Original Image", img)
cv.waitKey(0)
cv.destroyAllWindows()