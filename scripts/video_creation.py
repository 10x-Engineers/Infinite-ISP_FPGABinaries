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

# Supported Sensors and selected sensor (SENSOR)
SupportedSensors = {
    "AR1335": 1,
    "OV5647": 2 
}
SENSOR = "OV5647"

# Supported ISP output formats
Supported_Formats = {
    "RGB" : 1,
    "YUV" : 2
}

# Select the format by copying supported format string from above
Selected_Format = "YUV"

# Starting and ending frames of the video sequence
start_index, end_index = 1, 250

# Size of the output image
h, w =  1080, 1920

# parent directory
p = Path(path)
parent_dir = p.resolve().joinpath(SENSOR)

# Making directory for saving .png files
bin_dir = "Burst_Capture"       # Created by firmware, DO NOT MODIFY
bin_path = parent_dir / bin_dir
frame_dir = Selected_Format + '_Frames'
frame_path = parent_dir / frame_dir
video_dir = "Video_Frames"
video_path = parent_dir / video_dir
Path.mkdir(frame_path,exist_ok=True)
Path.mkdir(video_path,exist_ok=True) 

# Images are stored in the form of rows where the size of each row in bytes
# should be a multiple of 256, each such row size is called 'stride'
stride = np.floor(np.floor(np.floor((w*3 + 255) /256)) * 256)
stride = stride.astype(np.uint16)
img = np.zeros((h,w,3), dtype=np.uint8)

for m in range(start_index,end_index+1):
    # repalce the first number in the filename as per the iteration number 
    filename =str(bin_path) + '/' + Selected_Format + str(m) + '.bin'
    with open(filename, 'rb') as f:
        arr = np.fromfile(f, dtype=np.uint8)
    f.close()

    arr = np.reshape(arr, (h, stride))
    # print(arr.shape)

    arr_trun = arr[:,0:w*3]
    # print(arr_trun.shape)

    arr_flat = arr_trun.flatten()

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
        img[:,:,0] = R
        img[:,:,1] = G
        img[:,:,2] = B

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
if(Supported_Formats[Selected_Format] == Supported_Formats['YUV']):
    shutil.rmtree(image_folder)