"""
File: sensor_bin_to_sensor_raw_burst_capture.py
Description: converts the image sensor memory dumps (.bin) of
             RAW Burst Capture from the FPGA Platform to 
             Bayer RAW frames (.raw) containing valid pixel
             data.
             It also converts the Bayer RAW frames to
             equivalent grayscale .png for visualization.
Author: 10xEngineers
------------------------------------------------------------
"""
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from pathlib import Path

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

# start and end index of burst capture frames for converting .bin to .raw
start, end = 1, 193

# parent directory
p = Path(path)
parent_dir = p.resolve().joinpath(SENSOR)   

# Making directories for saving .raw and .png files
raw_dir = "BurstCapture_RAW"
png_dir = "BurstCapture_PNG"
bin_dir = "BurstCapture_Pairs/RAW"       # Created by firmware, DO NOT MODIFY
# joining paths with parent directory
raw_path = parent_dir/ raw_dir 
Path.mkdir(raw_path, exist_ok=True)
png_path = parent_dir / png_dir
Path.mkdir(png_path, exist_ok=True)
bin_path = parent_dir / bin_dir

# Selecting height and width based on selected sensor
if(SupportedSensors[SENSOR] == SupportedSensors["AR1335"]):
    h, w = 1536, 2048
    bits, bayer = 10, "GRBG"
    
if(SupportedSensors[SENSOR] == SupportedSensors["OV5647"]):
    h, w = 1944, 2592
    bits, bayer = 10, "BGGR"
    
if(SupportedSensors[SENSOR] == SupportedSensors["IMX219"]):
    h, w = 1944, 2592
    bits, bayer = 10, "RGGB"

h =  int(h)
w =  int(w)

# Images are stored in the form of rows where the size of each row in bytes
# should be a multiple of 256, each such row size is called 'stride'
# For raw10 format, 3 pixels are packed into 4 bytes
stride = np.floor(np.floor(np.floor((w+2)/3) *4 +256 - 1) /256) * 256
stride = stride.astype (np.uint16)
pixelsInStride= int((stride/4)*3)

for index in range (start, end+1):
# reading the dumped binary file
    filename = 'RAW_' + scene_name + '_' + str(w) + 'x' + str(h) + '_' + str(bits) + 'bits_' + bayer + '_' + str(index) + '.bin'
    filepath = bin_path / filename
    print('Processing ' + 'RAW'+ str(index) + ' ...')
    with open(filepath, 'rb') as f:
        # read the contents of the file into a new array
        arr = np.fromfile(f, dtype=np.uint8)

    # Reshape the array into groups of 4 elements
    grouped_array = arr.reshape(-1, 4)
    flipped_array = np.flip(grouped_array, axis=1)
    result_list = []
    for inner_array in flipped_array:
        # Convert each element to binary and concatenate
        binary_concatenated = ''.join([format(x, '08b') for x in inner_array])
        result_list.append((int(binary_concatenated[22:32],2),int(binary_concatenated[12:22],2),int(binary_concatenated[2:12],2)))
    img = np.array(result_list).reshape((h, pixelsInStride))[:, 0:w].astype(np.uint16)

    # dumping a .raw file for inf_isp
    filename = filename[:-4]
    extension = ".raw"

    with open('{}{}'.format(str(raw_path/filename),extension),'wb') as f:
        img.tofile(f)

    # dumping a numpy array
    img_norm = np.interp(img, (img.min(), img.max()), (0,1023 )).astype(np.uint8)
    plt.imshow(img_norm,cmap='gray').write_png(str(png_path/filename) + '.png')
