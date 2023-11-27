# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:07:11 2023

@author: 10xe
"""
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Supported Sensors

SENSOR = "OV5647"   #copy string from supported sensor type here

SupportedSensors = {
    "AR1335": 1,
    "OV5647": 2 
}

# reading the dumped binary file
filename = 'RAW_TestImage_2592x1944_10bits_BGGR.bin'
with open(filename, 'rb') as f:
    # read the contents of the file into a new array
    arr = np.fromfile(f, dtype=np.uint8)
    
if(SupportedSensors[SENSOR] == SupportedSensors["AR1335"]):
    h, w = 1536, 2048

if(SupportedSensors[SENSOR] == SupportedSensors["OV5647"]):
    h, w = 1944, 2592

h =  np.array (h, dtype = np.uint16)
w =  np.array (w, dtype = np.uint16)

# Images are stored in the form of rows where the size of each row in bytes
# should be a multiple of 256, each such row size is called 'stride'
stride = np.floor(np.floor(np.floor((w+2)/3) *4 +256 - 1) /256) * 256
stride = stride.astype (np.uint16)
print (stride)

# reshaping the input based on stride
arr = np.reshape(arr, (h, stride))
print (arr.shape)

raw = np.zeros ((h,w),dtype=np.uint16)
for i in range (0, h):
    k = 0
    for j in range (0, stride, 4):
        # data is stored in reversed order in form of 4 bytes for 3 pixels
        # so fliping it to get the correct data
        temp = np.flip(arr [i,j:j+4])  
        binary_str = ''.join(format(b, '08b') for b in temp)
        binary_num_3 = int((binary_str[2:12]), 2)
        binary_num_2 = int((binary_str[12:22]), 2)
        binary_num_1 = int((binary_str[22:32]), 2)
        # stride > no of cols, so discarding extra data
        if (k  > (w-1)):
            break
        raw[i,k] = np.uint16(binary_num_1)
        if (k +1 > (w-1)):
            break
        raw[i,k+1] = np.uint16(binary_num_2)
        if (k + 2 > (w-1)):
            break
        raw[i,k+2] = np.uint16(binary_num_3)
        k = k+3

img = raw.copy()
img = img.astype(np.uint16)

# dumping a .raw file for inf_isp
filename = filename[:-4]
extension = ".raw"
with open('{}{}'.format(filename,extension),'wb') as f:
    img.tofile(f)


# dumping a numpy array
img_norm = np.interp(img, (img.min(), img.max()), (0,1023 )).astype(np.uint8)
plt.imshow(img_norm,cmap='gray').write_png('./' + filename + '.png')
plt.show()
