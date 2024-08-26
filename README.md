# Infinite-ISP
Infinite-ISP is a full-stack ISP development platform designed for all aspects of a hardware ISP. It includes a collection of camera pipeline modules written in Python, a fixed-point reference model, an optimized RTL design, an FPGA integration framework and its associated firmware ready for Xilinx® Kria KV260 development board. The platform features a stand-alone Python-based Tuning Tool that allows tuning of ISP parameters for different sensors and applications. Finally, it also offers a software solution for Linux by providing required drivers and a custom application development stack to bring Infinite-ISP to the Linux platforms.


![](doc/assets/Infinite-ISP_Repo_Flow.png)

| Sr.     | Repository name        | Description      | 
|---------| -------------  | ------------- |
| 1  | **[Infinite-ISP_AlgorithmDesign](https://github.com/10x-Engineers/Infinite-ISP)**   | Python based model of the Infinite-ISP pipeline for algorithm development |
| 2  | **[Infinite-ISP_ReferenceModel](https://github.com/10x-Engineers/Infinite-ISP_ReferenceModel)**                      | Python based fixed-point model of the Infinite-ISP pipeline for hardware implementation |
| 3  | **[Infinite-ISP_RTL](https://github.com/10x-Engineers/Infinite-ISP_RTL)**  | RTL Verilog design of the image signal processor based on the Reference Model |
| 4  | **[Infinite-ISP_AutomatedTesting](https://github.com/10x-Engineers/Infinite-ISP_AutomatedTesting)**   | A framework to enable the automated block and multi-block level testing of the image signal processor to ensure a bit accurate design |
| 5  | **FPGA Implementation** | FPGA implementation of Infinite-ISP on <br>  <ul><li>Xilinx® Kria KV260’s XCK26 Zynq UltraScale + MPSoC **[Infinite-ISP_FPGA_XCK26](https://github.com/10x-Engineers/Infinite-ISP_FPGA_XCK26)** </li></ul>   |
| 6  | **[Infinite-ISP_FPGABinaries](https://github.com/10x-Engineers/Infinite-ISP_FPGABinaries)**  :anchor: | FPGA binaries (bitstream + firmware executable) for the Xilinx® Kria KV260’s XCK26 Zynq UltraScale + MPSoC|
| 7  | **[Infinite-ISP_TuningTool](https://github.com/10x-Engineers/Infinite-ISP_TuningTool)**                              | Collection of calibration and analysis tools for the Infinite-ISP |
| 8  | **[Infinite-ISP_LinuxCameraStack](https://github.com/10x-Engineers/Infinite-ISP_LinuxCameraStack.git)** | Extending Linux support to Infinite-ISP and the developement of Linux-based camera application stack |

**[Request Access](https://docs.google.com/forms/d/e/1FAIpQLSfOIldU_Gx5h1yQEHjGbazcUu0tUbZBe0h9IrGcGljC5b4I-g/viewform?usp=sharing)** to **Infinite-ISP_RTL, Infinite-ISP_AutomatedTesting** and **Infinite-ISP_FPGA_XCK26** repositories


# Infinite-ISP FPGA Binaries
Infinite-ISP Image Signal Processing Pipeline FPGA binaries for XCK26 Zynq® UltraScale+™ MPSoC present on Xilinx® Kria™ KV260 Vision AI Starter Kit. Each binary file includes an FPGA bitstream paired with its firmware executable.

# How to use the FPGA Binary Files

## v1.3 (CVPR2024 Demo)
### For IMX219 image sensor module:
#### (Raspberry Pi Camera Module v2 or other compatible IMX219 image sensor module)
1. Connect the IMX219 image sensor module to the RPi port on the Kria KV260 AI Starter Kit.
2. Insert an SD Card (2GB or above) into the Kria KV260 board.
3. Connect the Kria KV260 board with a monitor screen using an HDMI cable.
4. Power up the Kria KV260 board and follow the [steps](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+SOMs+Starter+Kits#Boot-Image-Recovery-Tool) for loading the on-board Xilinx Image Recovery Tool.
5. Upload the desired binary file (e.g. Infinite-ISP_v1.3-IMX219.bin) provided in the release on the Kria KV260 AI Starter Kit.
6. Reset the Kria KV260 board and visualize the Infinite-ISP output on your monitor screen.
7. Connect the USB cable with the JTAG/USB port on Kria to read the messages over the serial interface (baud rate 115200).
8. A configuration menu as shown below will appear. Details of the user menu are provided in the [user guide](https://github.com/10x-Engineers/Infinite-ISP_FPGABinaries/blob/main/doc/Infinite-ISP%20Configuration%20Menu.md): 

<kbd>![status before dumping](/doc/v1.3/imx219_user_menu.png)</kbd>

9. If you want to dump frame(s), do so by going to option 2, and then you can remove the SD card from the Kria board.

10. Extract the dumped frame(s) from the SD card and visualize them using the provided [scripts](/scripts).

### For AR1335 IAS module:
1. Connect AR1335 IAS image sensor module to the IAS1 port on Kria KV260 AI Starter Kit.
2. Insert SD Card (2GB or above) into the Kria KV260 board.
3. Connect the Kria KV260 board with a monitor screen using an HDMI cable.
4. Power up the Kria KV260 board and follow the [steps](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+SOMs+Starter+Kits#Boot-Image-Recovery-Tool) for loading the on-board Xilinx Image Recovery Tool.
5. Upload the desired binary file (e.g. Infinite-ISP_v1.3-AR1335.bin) provided in the release on the Kria KV260 AI Starter Kit.
6. Reset the Kria KV260 board and visualize the Infinite-ISP output on your monitor screen.
7. Connect the USB cable with the JTAG/USB port on Kria to read the messages over the serial interface (baud rate 115200).
8. A configuration menu as shown below will appear. Details of the user menu are provided in the [user guide](https://github.com/10x-Engineers/Infinite-ISP_FPGABinaries/blob/main/doc/Infinite-ISP%20Configuration%20Menu.md):

<kbd>![status before dumping](/doc/v1.3/ar1335_user_menu.png)</kbd> 

9. If you want to dump frame(s), do so by going to option 2, and then you can remove the SD card from the Kria board.

10. Extract the dumped frame(s) from the SD card and visualize them using the provided [scripts](/scripts).

### For OV5647 image sensor module:
#### (Raspberry Pi Camera Module v1 or other compatible OV5647 image sensor module)
1. Connect the OV5647 image sensor module to the RPi port on the Kria KV260 AI Starter Kit.
2. Insert an SD Card (2GB or above) into the Kria KV260 board.
3. Connect the Kria KV260 board with a monitor screen using an HDMI cable.
4. Power up the Kria KV260 board and follow the [steps](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+SOMs+Starter+Kits#Boot-Image-Recovery-Tool) for loading the on-board Xilinx Image Recovery Tool.
5. Upload the desired binary file (e.g. Infinite-ISP_v1.3-OV5647.bin) provided in the release on the Kria KV260 AI Starter Kit.
6. Reset the Kria KV260 board and visualize the Infinite-ISP output on your monitor screen.
7. Connect the USB cable with the JTAG/USB port on Kria to read the messages over the serial interface (baud rate 115200).
8. A configuration menu as shown below will appear. Details of the user menu are provided in the [user guide](https://github.com/10x-Engineers/Infinite-ISP_FPGABinaries/blob/main/doc/Infinite-ISP%20Configuration%20Menu.md):

<kbd>![status before dumping](/doc/v1.3/ov5647_user_menu.png)</kbd>

9. If you want to dump frame(s), do so by going to option 2, and then you can remove the SD card from the Kria board.

10. Extract the dumped frame(s) from the SD card and visualize them using the provided [scripts](/scripts).

## v1.2
### For AR1335 IAS module:
1. Connect AR1335 IAS image sensor module to the IAS1 port on Kria KV260 AI Starter Kit.
2. Insert SD Card (2GB or above) into the Kria KV260 board.
3. Connect the Kria KV260 board with a monitor screen using an HDMI cable.
4. Power up the Kria KV260 board and follow the [steps](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+SOMs+Starter+Kits#Boot-Image-Recovery-Tool) for loading the on-board Xilinx Image Recovery Tool.
5. Upload the desired binary file (e.g. Infinite-ISP_v1.2-AR1335.bin) provided in the release on the Kria KV260 AI Starter Kit.
6. Reset the Kria KV260 board and visualize the Infinite-ISP output on your monitor screen.
7. Connect the USB cable with the JTAG/USB port on Kria to read the messages over the serial interface (baud rate 115200).
8. A configuration menu as shown below will appear. Details of the user menu are provided in the [user guide](https://github.com/10x-Engineers/Infinite-ISP_FPGABinaries/blob/release_v1.2/doc/Infinite-ISP%20Configuration%20Menu.md):

<kbd>![status before dumping](/doc/v1.2/user_menu.png)</kbd> 

9. If you want to dump frame(s), do so by going to option 2, and then you can remove the SD card from the Kria board.

10. Extract the dumped frame(s) from the SD card and visualize them using the provided [scripts](/scripts).

### For OV5647 image sensor module:
1. Connect the OV5647 image sensor module to the RPi port on the Kria KV260 AI Starter Kit.
2. Insert an SD Card (2GB or above) into the Kria KV260 board.
3. Connect the Kria KV260 board with a monitor screen using an HDMI cable.
4. Power up the Kria KV260 board and follow the [steps](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+SOMs+Starter+Kits#Boot-Image-Recovery-Tool) for loading the on-board Xilinx Image Recovery Tool.
5. Upload the desired binary file (e.g. Infinite-ISP_v1.2-OV5647.bin) provided in the release on the Kria KV260 AI Starter Kit.
6. Reset the Kria KV260 board and visualize the Infinite-ISP output on your monitor screen.
7. Connect the USB cable with the JTAG/USB port on Kria to read the messages over the serial interface (baud rate 115200).
8. RAW-ISPout image pair and Burst Capture frames dump in SD Card status will be displayed over serial interface:

<kbd>![status before dumping](/doc/v1.2/user_menu_1.png)</kbd>

9. If you want to dump frame(s), do so by going to option 2, and then you can remove the SD card from the Kria board.

10. Extract the dumped frame(s) from the SD card and visualize them using the provided [scripts](/scripts).

## v1.1
### For AR1335 IAS module:
1. Connect AR1335 IAS image sensor module to the IAS1 port on Kria KV260 AI Starter Kit.
2. Insert SD Card (2GB or above) into the Kria KV260 board.
3. Connect the Kria KV260 board with a monitor screen using HDMI cable.
4. Power up the Kria KV260 board and follow the [steps](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+SOMs+Starter+Kits#Boot-Image-Recovery-Tool) for loading the on-board Xilinx Image Recovery Tool.
5. Upload the desired binary file (e.g. Infinite-ISP_v1.1-AR1335-1080p.bin) provided in the release on the Kria KV260 AI Starter Kit.
6. Reset the Kria KV260 board and visualize the Infinite-ISP output on your monitor screen.
7. Connect the USB cable with the JTAG/USB port on Kria to read the messages over serial interface (baud rate 115200).
8. RAW-ISPout image pair and Burst Capture frames dump in SD Card status will be displayed over serial interface:

<kbd>![status before dumping](/doc/v1.1/ar1335_1.png)</kbd> 

9. Once SD Card dumps are complete, you can remove the SD card from the Kria board.

<kbd>![status after dumping](/doc/v1.1/ar1335_2.png)</kbd> 

10. Extract the dumped single RAW-ISPout pair and Burst Capture frames from the SD card and visualize them using provided [scripts](/scripts).

### For OV5647 image sensor module:
1. Connect OV5647 image sensor module to the RPi port on Kria KV260 AI Starter Kit.
2. Insert SD Card (2GB or above) into the Kria KV260 board.
3. Connect the Kria KV260 board with a monitor screen using HDMI cable.
4. Power up the Kria KV260 board and follow the [steps](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+SOMs+Starter+Kits#Boot-Image-Recovery-Tool) for loading the on-board Xilinx Image Recovery Tool.
5. Upload the desired binary file (e.g. Infinite-ISP_v1.1-OV5647-1080p.bin) provided in the release on the Kria KV260 AI Starter Kit.
6. Reset the Kria KV260 board and visualize the Infinite-ISP output on your monitor screen.
7. Connect the USB cable with the JTAG/USB port on Kria to read the messages over serial interface (baud rate 115200).
8. RAW-ISPout image pair and Burst Capture frames dump in SD Card status will be displayed over serial interface:

<kbd>![status before dumping](/doc/v1.1/ov5647_1.png)</kbd>

9. Once SD Card dumps are complete, you can remove the SD card from the Kria board.

<kbd>![status before dumping](/doc/v1.1/ov5647_2.png)</kbd>

10. Extract the dumped single RAW-ISPout pair and Burst Capture frames from the SD card and visualize them using provided [scripts](/scripts).

## v1.0
1. Connect the AR1335 IAS image sensor module (included in Xilinx Kria KV260 Accessory Pack) to the IAS1 port on the Kria KV260 AI Starter Kit.
2. Insert an SD Card (2GB or above) into the Kria KV260 board.
3. Connect the Kria KV260 board with a monitor screen using an HDMI cable.
4. Power up the Kria KV260 board and follow the [steps](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+SOMs+Starter+Kits#Boot-Image-Recovery-Tool) for loading the on-board Xilinx Image Recovery Tool.
5. Upload the desired binary file (e.g. 'Infinite-ISP_v1.0-1080p.bin') on the Kria KV260 AI Starter Kit.
6. Reset the Kria KV260 board and visualize the Infinite-ISP output on your monitor screen.
7. Connect the USB cable with the JTAG/USB port on Kria to read the messages over serial interface (baud rate 115200).
8. You can remove the SD card from the Kria board, extract the dumped single RGB-RAW pair and 300 RGB frames (if applicable), and visualize them using the provided scripts.

## Scripts for visualization of FPGA outputs in SD Card
| Name | Description |
| -----| ----- |
| sensor_bin_to_sensor_raw.py | converts the image sensor memory dump (.bin) data from the FPGA Platform to Bayer RAW frame (.raw) containing valid pixel data. |
| isp_output_bin_to_isp_output_png.py | converts the ISP output memory dump (.bin) data from the FPGA Platform to output image frame (.png) as well as output pixel data frame (.bin) for verification. |
| sensor_bin_to_sensor_raw_burst_capture.py | converts the image sensor memory dumps (.bin) of RAW Burst Capture from the FPGA Platform to Bayer RAW frames (.raw) containing valid pixel data. It also converts the Bayer RAW frames to equivalent grayscale .png for visualization. |
| video_creation.py | converts multiple ISP output memory dumps (.bin) from the FPGA Platform to corresponding output image frames (.png) and stitches them together into a .mp4 video. |

## Contact
For any inquiries or feedback, feel free to reach out.

Email: isp@10xengineers.ai

Website: http://www.10xengineers.ai

LinkedIn: https://www.linkedin.com/company/10x-engineers/
