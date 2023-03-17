#!/usr/bin/env python3
#!interpreter [optional-arg]
__author__ = "Arun Gopinathan"
__credits__ = ["Arun Gopinathan",'Rajeev Raveendran']
__license__ = "GNU GPL"
__version__ = "0.0.1"
__maintainer__ = "Arun Gopinath"
__email__ = "garunalways@gmail.com"
__status__ = "Production"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import os.path, sys


# Add path containing FESEM images
path = "demo"
dirs = os.listdir(path)

# Function to calculate 2D Fourier Tranform
def calculate_2dft(input):
    ft = np.fft.ifftshift(input)
    ft = np.fft.fft2(ft)
    return np.fft.fftshift(ft)

# This function will crop the image to remove FESEM databar and
# each image is converted into Fourier Transform. Both images are savedin same folder
def crop_ft():
    for item in dirs:
        fullpath = os.path.join(path,item)       
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((174.5, 0, 849.5, 675)) # cropping databar
            imCrop.save(f + '_Cropped.png', "png", quality=100) # saving cropped image as png
            image = np.array(imCrop)

            # Read and process image
            #image = mpimg.imread(fullpath)
            image = image[:, :, :3].mean(axis=2)
            plt.set_cmap("gray") # Try - hot,gray, Greens, plasma, cividis, inferno, gist_earth (more on colormap - matplotlib)
            ft = calculate_2dft(image)

            # Plotting is done in log scale 
            plt.imshow(np.log(abs(ft))) # You can remove np.log to check the normal results
            plt.axis("off") # To remove the axis

            # If you are sure about the limits, then remove the hash and edit xlim and ylim (better around center)
            plt.xlim([0, 675])
            plt.ylim([0, 675])
            plt.savefig(f + '_fourier.png') # Saving the final FT image
crop_ft()
