import numpy as np

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

# Replace 'example.bin' with the path to your binary file
file_path = 'RAW_TestImage_1952x1112_10bits_RGGB.bin'

# Read the binary file
file_contents = read_bin_file(file_path)

# Array for storing the correct bytes order
new_array = np.zeros(int(file_contents.__len__()/4),dtype=np.uint16)

# Extracting RAW pixel from 4 bytes and putting it in 2 bytes
# xx_RAW10-P0_RAW10-P0_RAW10-P0 --> xxxxxx_RAW10-P0
for n in range(int((file_contents.__len__())/4)):
    new_array[n] = ((file_contents[n*4 + 2] & 0x03) << 8) | ((file_contents[n*4 + 3] & 0xFF))

# Writing the new_array contents to the RAW output file
with open(file_path[:-3]+'raw', 'wb') as file:
    # Write the new contents to a new binary file
    file.write(new_array)
