# How to use the Titanium Ti180 J484 Binary Files

## v1.3.1
### For IMX219 image sensor module:
#### (Raspberry Pi Camera Module v2 or other compatible IMX219 image sensor module)
1. Connect the IMX219 image sensor module to the P1 connector on the Titanium Ti180 J484 Development Kit.
2. Insert an SD Card (2GB or above) into the Titanium Ti180 board.
3. Connect the Titanium Ti180 board with a monitor screen using an HDMI cable.
4. Power up the Titanium Ti180 board and follow the [steps](https://www.efinixinc.com/docs/efinity-pgm-v3.3.pdf) on page 7 to upload binary.
5. Upload the desired binary file (e.g. Infinite-ISP_v1.3.1-IMX219.hex) provided in the release on the Titanium Ti180 J484 Development Kit.
6. Reset the Titanium Ti180 board by turning it OFF and then ON and visualize the Infinite-ISP output on your monitor screen.
7. Connect the USB cable with the JTAG/USB port on Titanium Ti180 to read the messages over the serial interface (baud rate 115200).
8. A ISP Example Design Scenario Selection as shown below will appear. Always select `e mode` to visualize the output.

<kbd>![status before dumping](../../doc/efinix_ti180/v1.3.1/imx219_scenario_selection.png)</kbd>

9. To enable/disable the FPS Statistics press `z` and it will be shown as:

<kbd>![status before dumping](../../doc/efinix_ti180/v1.3.1/imx219_FPS.png)</kbd>

10. If you want to dump frame(s), to do so press `u` for RAW dump, `v` for RGB dump, and `s` (recommended) to dump frames in RAW/RGB pair, and then you can remove the SD card from the Titanium Ti180 board.

<kbd>![status before dumping](../../doc/efinix_ti180/v1.3.1/imx219_dump_frames.png)</kbd>

11. Extract the dumped frame(s) from the SD card and visualize them using the provided [scripts](../../scripts/efinix_ti180).

## Scripts for visualization of FPGA outputs in SD Card
| Name | Description |
| -----| ----- |
| sd_reader_raw_ispout_pair.sh | extract the image sensor memory dump data from the SD Card. |
| efinix_rgb_conversion.py | converts the RGB output memory dump (.bin) data from the FPGA Platform to output image frame (.png) as well as output pixel data frame (.bin) for verification. |
| efinix_raw_conversion.py | converts the image sensor memory dump (.bin) of RAW Burst Capture from the FPGA Platform to Bayer RAW frames (.raw) containing valid pixel data. |