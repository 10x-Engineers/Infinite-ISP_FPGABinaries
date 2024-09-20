"""
File: video_creation.py
Description: converts multiple ISP output memory dumps (.bin)
             from the FPGA Platform to corresponding output 
             image frames (.png) and stitches them together 
             into a .mp4 video
Author: 10xEngineers
------------------------------------------------------------
"""

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path
import cv2
import os
import shutil

# Path of the directory containing "OV5467" and "AR1335" directories
path =  "./"
scene_name = "TestImage"

# Supported Sensors and selected sensor (SENSOR)
SupportedSensors = {
    "AR1335": 1,
    "OV5647": 2,
    "IMX219": 3 
}
SENSOR = "AR1335"

# Supported ISP output formats
Supported_Formats = {
    "RGB" : 1,
    "YUV" : 2
}

# Select the format by copying supported format string from above
Selected_Format = "RGB"

# Starting and ending frames of the video sequence
start_index, end_index = 1, 193

# Size of the output image
h, w =  1080, 1920

# Selecting bits and bayer based on selected sensor
if(SupportedSensors[SENSOR] == SupportedSensors["AR1335"]):
    sns_width, sns_height = 2048, 1536
    bits, bayer = 10, "GRBG"
    
if(SupportedSensors[SENSOR] == SupportedSensors["OV5647"]):
    sns_width, sns_height = 2592, 1944
    bits, bayer = 10, "BGGR"
    
if(SupportedSensors[SENSOR] == SupportedSensors["IMX219"]):
    sns_width, sns_height = 2592, 1944
    bits, bayer = 10, "RGGB"

# parent directory
p = Path(path)
parent_dir = p.resolve().joinpath(SENSOR)

# Making directory for saving .png files
bin_dir = "BurstCapture_Pairs/ISPout"       # Created by firmware, DO NOT MODIFY
bin_path = parent_dir / bin_dir
frame_dir = Selected_Format + '_Frames'
frame_path = parent_dir / frame_dir
fpga_dir = "FPGA_Bins"
fpga_path = parent_dir / fpga_dir
video_dir = "Video_Frames"
video_path = parent_dir / video_dir
Path.mkdir(frame_path,exist_ok=True)
Path.mkdir(video_path,exist_ok=True)
Path.mkdir(fpga_path,exist_ok=True)  

# Images are stored in the form of rows where the size of each row in bytes
# should be a multiple of 256, each such row size is called 'stride'
stride = np.floor(np.floor(np.floor((w*3 + 255) /256)) * 256)
stride = stride.astype(np.uint16)
img = np.zeros((h,w,3), dtype=np.uint8)

for m in range(start_index,end_index+1):
    # repalce the first number in the filename as per the iteration number
    filepath = str(bin_path) + '/' 
    filename = Selected_Format + '_' + scene_name + '_' + str(sns_width) + 'x' + str(sns_height) + '_' + str(bits) + 'bits_' + bayer + '_' + str(m) + '.bin'
    with open(filepath + filename, 'rb') as f:
        arr = np.fromfile(f, dtype=np.uint8)
    f.close()

    arr = np.reshape(arr, (h, stride))
    # print(arr.shape)

    arr_trun = arr[:,0:w*3]
    # print(arr_trun.shape)

    # flatten the shape
    arr_flat = arr_trun.flatten()
    arr_flat_u16 = arr_flat.astype(np.uint16)
    arr_corrected = np.zeros(arr_flat_u16.shape, dtype=np.uint16)

    # reversing the order since the file that came from FPGA is BGR/VUY BGR/VUY BGR/VUY ...
    arr_corrected[0::3] = arr_flat[0::3]
    arr_corrected[1::3] = arr_flat[1::3]
    arr_corrected[2::3] = arr_flat[2::3]
    
    # dumping the strides removed binary file in the FPGA_Bin directory
    arr_corrected.tofile(str(fpga_path) + '/' + "FPGA" + filename)

    R_flat = arr_flat[0::3]
    G_flat = arr_flat[1::3]
    B_flat = arr_flat[2::3]

    R = R_flat.reshape(h,w)
    G = G_flat.reshape(h,w)
    B = B_flat.reshape(h,w)

    # In case of RGB, switch the 1st and the 3rd channels
    img[:,:,0] = B
    img[:,:,1] = G
    img[:,:,2] = R

    # Creating RGB/YUV frames in RGB_Frames or YUV_Frames directory
    plt.imsave(str(frame_path) + '/' + str(m) +'.png', img[:,:,:])

    if(Supported_Formats[Selected_Format] == Supported_Formats["YUV"]):
        # In case of YUV, don't switch the 1st and the 3rd channels
        img[:,:,0] = B
        img[:,:,1] = G
        img[:,:,2] = R

        # Converting YUV frame to RGB frame
        img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR)
        plt.imsave(str(video_path) + '/' + str(m) +'.png', img[:,:,:])

    print(str(m)+'/'+str(end_index))


# Path to the folder containing the PNG images
if(Supported_Formats[Selected_Format] == Supported_Formats['YUV']):
    image_folder = str(video_path)
else:
    image_folder = str(frame_path)

# Output video file name
video_name = 'Video.mp4'

# Frame rate of the output video
if(SupportedSensors[SENSOR] == SupportedSensors['AR1335']):
    fps = 30

if(SupportedSensors[SENSOR] == SupportedSensors['OV5647']):
    fps = 15
    
if(SupportedSensors[SENSOR] == SupportedSensors['IMX219']):
    fps = 20

# Function to sort the images numerically
def sort_key(s):
    return int(os.path.splitext(s)[0])

# Get the list of PNG image file names in the folder
images = [img for img in os.listdir(image_folder) if img.endswith('.png')]
images.sort(key=sort_key)

# Get the first image to extract the frame size
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(str(frame_path) + '/' + video_name, fourcc, fps, (width, height))

# Iterate over the images and write each frame to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    video.write(frame)

# Release the video writer and close any open windows
video.release()
cv2.destroyAllWindows()

# Remove directory after creating RGB video for YUV
shutil.rmtree(str(video_path))
