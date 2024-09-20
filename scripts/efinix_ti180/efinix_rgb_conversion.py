"""
File: efinix_rgb_conversion.py
Description: converts the ISP output memory dump (.bin) data
             from the Efinix FPGA Platform to output image
             frame (.png)  as well as output pixel data
             frame (.bin) for verification
Author: 10xEngineers
------------------------------------------------------------
"""

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from datetime import datetime

# Function for reading binary file contents
def read_bin_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Read the entire contents of the file
            contents = file.read()
            return contents
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# Set the debug flag
DEBUG_FLAG = 0

# Set the path and name of your binary file
file_path = './'
file_name = 'RGB_TestImage_1920x1080_8bits_RGB.bin'

# Read the binary file
file_contents = read_bin_file(file_path + file_name)

# Set dimensions of image to read and convert
w, h = 1920, 1080

# Array for storing the correct bytes order
new_array_red = np.zeros(int(file_contents.__len__()/4),dtype=np.uint8)
new_array_green = np.zeros(int(file_contents.__len__()/4),dtype=np.uint8)
new_array_blue = np.zeros(int(file_contents.__len__()/4),dtype=np.uint8)
new_array = np.zeros(int((file_contents.__len__()/4)*3),dtype=np.uint16)

# Extracting RGB pixels from 4 bytes and putting it in 1 byte
# byte order:   3_2_1_0
# data:         xxxxxxxx_B-P0_G-P0_R-P0 (mem_32b) --> R-P0_G-P0_B-P0_xxxxxxxx (sd_32b)--> R-P0, G-P0, B-P0
for n in range(int((file_contents.__len__())/4)):
    new_array_red[n]    = (file_contents[n*4 + 3] & 0xFF)
    new_array_green[n]  = (file_contents[n*4 + 2] & 0xFF)
    new_array_blue[n]   = (file_contents[n*4 + 1] & 0xFF)

# Storing in BGR format (Red at little end address)
new_array[0::3] = new_array_red[::]
new_array[1::3] = new_array_green[::]
new_array[2::3] = new_array_blue[::]

## Save the .bin file for FPGA verification
new_array.tofile(file_path + "FPGA_ISPout_" + file_name)

# Writing the new_array contents to the RAW output file
#with open(file_path[:-3]+'raw', 'wb') as file:
#    # Write the new contents to a new binary file
#    file.write(new_array)

R_flat = new_array[0::3]
G_flat = new_array[1::3]
B_flat = new_array[2::3]
R = R_flat.reshape(h,w)
G = G_flat.reshape(h,w)
B = B_flat.reshape(h,w)
img = np.zeros((h, w, 3), dtype=np.uint8)
img[:,:,0] = R
img[:,:,1] = G
img[:,:,2] = B

plt.imsave(file_path + 'FPGA_ISPout_' + file_name[:-4] + '.png', img.astype(np.uint8))
if (DEBUG_FLAG):
    plt.imshow(img)
    plt.show()
