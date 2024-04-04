# Taking a DNG Image  
from picamera2 import PiCamera2
import time

def capture_dng_image(output_file):
    # Open the camera
    with PiCamera2() as picam2:
        # Set resolution and format for High Quality Camera
        picam2.resolution = (3280, 2464) #4056 x 3040 pixels
        picam2.framerate = 15 #can change this value
        # Wait for the camera to warm up
        time.sleep(2)
        
        # Capture an image in DNG format
        picam2.capture(output_file, format='jpeg', bayer=True)

    print("Image captured as", output_file)

if __name__ == "__main__":
    output_file = "captured_image.dng"
    capture_dng_image(output_file)



# Tiff 
import rawpy
from PIL import Image

def convert_dng_to_tiff(input_file):
    # Load the DNG image
    with rawpy.imread(input_file) as raw:
        # Convert the DNG image to RGB
        rgb = raw.postprocess()

    # Create a PIL image from the RGB data
    image = Image.fromarray(rgb)

    # Save the image as TIFF
    tiff_output_file = input_file.replace('.dng', '.tiff')
    image.save(tiff_output_file, format='TIFF')

    print("Image saved as", tiff_output_file)

if __name__ == "__main__":
    input_file = "input_image.dng"  # Replace with the path to your DNG file
    convert_dng_to_tiff(input_file)



# Convert Tiff to Grayscale 
from PIL import Image

def convert_to_grayscale(input_file):
    # Open the TIFF image
    with Image.open(input_file) as img:
        # Convert the image to grayscale
        grayscale_img = img.convert('L')

    # Save the grayscale image
    grayscale_output_file = input_file.replace('.tiff', '_grayscale.tiff')
    grayscale_img.save(grayscale_output_file)

    print("Grayscale image saved as", grayscale_output_file)

if __name__ == "__main__":
    input_file = "input_image.tiff"  # Replace with the path to your TIFF file
    convert_to_grayscale(input_file)