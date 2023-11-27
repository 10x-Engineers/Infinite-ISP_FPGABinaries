import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from datetime import datetime
import cv2
import os

filepath = './ov5647/Burst_Capture/'
dest = './ov5647/Video_Frames/'
h, w =  1080, 1920
stride = np.floor(np.floor(np.floor((w*3 + 255) /256)) * 256)
stride = stride.astype(np.uint16)
img = np.zeros((h,w,3), dtype=np.uint8)

Supported_Formats = {
    "RGB" : 1,
    "YUV" : 2
}

# Select the format by copying supported format string from above
Selected_Format = "YUV"

start_index = 1
end_index = 250

for m in range(start_index,end_index+1):
    # repalce the first number in the filename as per the iteration number 
    filename =filepath + Selected_Format + str(m) + '.bin'
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


    img[:,:,0] = B
    img[:,:,1] = G
    img[:,:,2] = R

    plt.imsave(dest + str(m) +'.png', img[:,:,:])
    print(str(m)+'/'+str(end_index))


# Path to the folder containing the PNG images
image_folder = dest

# Output video file name
video_name = 'Video.mp4'

# Frame rate of the output video
fps = 30

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
video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

# Iterate over the images and write each frame to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    video.write(frame)

# Release the video writer and close any open windows
video.release()
cv2.destroyAllWindows()
