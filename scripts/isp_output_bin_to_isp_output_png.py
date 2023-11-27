import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from datetime import datetime


filepath = "./"
filename = 'ISPOut_TestImage_2592x1944_10bits_BGGR.bin'
with open(filepath + filename, 'rb') as f:
    arr = np.fromfile(f, dtype=np.uint8)
f.close()

h, w, Format, CONV_STD = 1080, 1920, "YUV444", 2   #copy string from support output formats here

SupportedFormats = {
    "BGR"   : 1,
    "YUV444": 2,
    "YUV422": 3
}

def yuv_to_rgb(yuv_img):
    """
    YUV-to-RGB Colorspace conversion 8bit
    """

    # make nx3 2d matrix of image
    mat_2d = yuv_img.reshape(
        (yuv_img.shape[0] * yuv_img.shape[1], 3)
    )

    # convert to 3xn for matrix multiplication
    mat2d_t = mat_2d.transpose()

    # subract the offsets
    mat2d_t = mat2d_t - np.array([[16, 128, 128]]).transpose()

    if CONV_STD == 1:
        # for BT. 709
        yuv2rgb_mat = np.array([[74, 0, 114], [74, -13, -34], [74, 135, 0]])
    else:
        # for BT.601/407
        # conversion metrix with 8bit integer co-efficients - m=8
        yuv2rgb_mat = np.array([[64, 87, 0], [64, -44, -20], [61, 0, 105]])

    # convert to RGB
    rgb_2d = np.matmul(yuv2rgb_mat, mat2d_t)
    rgb_2d = rgb_2d >> 6

    # reshape the image back
    rgb2d_t = rgb_2d.transpose()
    yuv_img = rgb2d_t.reshape(yuv_img.shape).astype(np.float32)

    # clip the resultant img as it can have neg rgb values for small Y'
    yuv_img = np.float32(np.clip(yuv_img, 0, 255))

    # convert the image to [0-255]
    yuv_img = np.uint8(yuv_img)
    return yuv_img

def reconstruct_yuv_from_422_custom(yuv_422_custom, width, height):
    """
    Reconstruct a YUV from YUV 422 format
    """
    # Create an empty 3D YUV image (height, width, channels)
    yuv_img = np.zeros((height, width, 3), dtype=np.uint8)
    # Rearrange the flattened 4:2:2 YUV data back to 3D YUV format
    yuv_img[:, 0::2, 0] = yuv_422_custom[0::4].reshape(height, -1)
    yuv_img[:, 0::2, 1] = yuv_422_custom[1::4].reshape(height, -1)
    yuv_img[:, 1::2, 0] = yuv_422_custom[2::4].reshape(height, -1)
    yuv_img[:, 0::2, 2] = yuv_422_custom[3::4].reshape(height, -1)
    # Replicate the U and V (chroma) channels to the odd columns
    yuv_img[:, 1::2, 1] = yuv_img[:, 0::2, 1]
    yuv_img[:, 1::2, 2] = yuv_img[:, 0::2, 2]
    return yuv_img

def reconstruct_yuv_from_444_custom(yuv_444_custom, width, height):
    """
    Reconstruct a YUV from YUV 444 format
    """
    # Create an empty 3D YUV image (height, width, channels)
    yuv_img = np.zeros((height, width, 3), dtype=np.uint8)
    # Rearrange the flattened 4:4:4 YUV data back to 3D YUV format
    yuv_img[:, 0::1, 0] = yuv_444_custom[0::3].reshape(height, -1)
    yuv_img[:, 0::1, 1] = yuv_444_custom[1::3].reshape(height, -1)
    yuv_img[:, 0::1, 2] = yuv_444_custom[2::3].reshape(height, -1)
    return yuv_img

def get_image_from_yuv_format_conversion(yuv_img, height, width, yuv_custom_format):
    """
    Convert YUV image into RGB based on its format & Conversion Standard
    """

    # Reconstruct the 3D YUV image from the custom given format YUV data
    if yuv_custom_format == "422":
        yuv_img = reconstruct_yuv_from_422_custom(yuv_img, width, height)
    else:
        yuv_img = reconstruct_yuv_from_444_custom(yuv_img, width, height)

    return yuv_img

def reconstrct_yuv422_for_rtl(arr, height, width):
    """Reconstruct a YUV from YUV 422 format."""

    # Create an empty 3D YUV image (height, width, channels)
    rtl_img = np.zeros((height * width * 2,), dtype=np.uint16)

    # select y, u and v channels from the binary input array
    arr_y = arr[2::3]
    arr_c = arr[1::3]

    # Rearrange the channels to construct 3D YUV image
    rtl_img[0::2] = arr_y
    rtl_img[1::2] = arr_c

    return rtl_img

stride = np.floor(np.floor(np.floor((w*3 + 255) /256)) * 256).astype(np.uint16)
arr = np.reshape(arr, (h, stride))

#Remove the extra zeros
arr_trun = arr[:,0:w*3]


#flatten the shape
arr_flat = arr_trun.flatten()
arr_flat_u16 = arr_flat.astype(np.uint16)
arr_corrected = np.zeros(arr_flat_u16.shape, dtype=np.uint16)


# reversing the order since the file that came from FPGA is BGR/YUV BGR/YUV BGR/YUV ...
arr_corrected[0::3] = arr_flat[2::3]
arr_corrected[1::3] = arr_flat[1::3]
arr_corrected[2::3] = arr_flat[0::3]
print('shape of final saved array ', arr_corrected.shape)
print(arr_corrected.dtype)

arr_corrected.tofile(filepath + "FPGA" + filename[3:])

#For displaying the saved image

if(SupportedFormats[Format] == SupportedFormats["BGR"]):
    R_flat = arr_corrected[0::3]
    G_flat = arr_corrected[1::3]
    B_flat = arr_corrected[2::3]
    R = R_flat.reshape(h,w)
    G = G_flat.reshape(h,w)
    B = B_flat.reshape(h,w)
    img = np.zeros((h, w, 3), dtype=np.uint8)
    img[:,:,0] = R
    img[:,:,1] = G
    img[:,:,2] = B

if(SupportedFormats[Format] == SupportedFormats["YUV444"]):
    YUV_img = get_image_from_yuv_format_conversion(arr_flat, h, w, "444")
    img = yuv_to_rgb(YUV_img)

if(SupportedFormats[Format] == SupportedFormats["YUV422"]):
    YUV422_img = reconstrct_yuv422_for_rtl(arr_corrected, h, w)
    YUV_img = get_image_from_yuv_format_conversion(YUV422_img, h, w, "422")
    img = yuv_to_rgb(YUV_img)

plt.imshow(img)
plt.imsave(filepath + 'FPGA' + filename[3:-4] + '.png', img.astype(np.uint8))
plt.show()
