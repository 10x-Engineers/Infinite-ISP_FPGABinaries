# Infinite-ISP
Infinite-ISP is a one stop solution for all your ISP development needs - from algorithms to an FPGA prototype and associated firmware, tools, etc. Its primary goal is to offer a unified platform that empowers ISP developers to accelerate ISP innovation. It includes a complete collection of camera pipeline modules written in Python, an FPGA bit-stream & the associated firmware for the implementation of the pipeline on the Kria KV260 development board and lastly a stand-alone Python based Tuning tool application for the pipeline.  The main components of the Infinite-ISP project are listed below:

| Repository name        | Description      | 
| -------------  | ------------- |
| **[Infinite-ISP_AlgorithmDesign](https://github.com/xx-isp/infinite-isp)**                        | Python based model of the Infinite-ISP pipeline for algorithm development |
| **[Infinite-ISP_ReferenceModel](https://github.com/10xEngineersTech/Infinite-ISP_ReferenceModel)**                       | Python based fixed-point model of the Infinite-ISP pipeline for hardware implementation |
| **[Infinite-ISP_FPGABinaries](https://github.com/10xEngineersTech/Infinite-ISP_FPGA_Binaries)** :anchor:                                     | FPGA binaries for the Kria KV260’s Xilinx® XCK26 Ultrascale FPGA|
| **[Infinite-ISP_Firmware](https://github.com/10xEngineersTech/Infinite-ISP_Firmware)**                                      | Firmware for the Kria KV260’s embedded Arm® Cortex®A53 processor|
| **[Infinite-ISP_TuningTool](https://github.com/10xEngineersTech/Infinite-ISP_TuningTool)**                              | Collection of calibration and analysis tools for the Infinite-ISP |


# Infinite-ISP_FPGA_Binaries
Infinite-ISP Image Signal Processing Pipeline FPGA binaries for XCK26 Zynq® UltraScale+™ MPSoC present on Xilinx® Kria™ KV260 Vision AI Starter Kit

# How to use the FPGA Binary Files
1. Connect AR1335 IAS image sensor module (included in Xilinx Kria KV260 Accessory Pack) to the IAS1 port on Kria KV260 AI Starter Kit.
2. Insert SD Card (2GB or above) into the Kria KV260 board.
3. Connect the Kria KV260 board with a monitor screen using HDMI cable.
4. Power up the Kria KV260 board and follow the [steps](https://docs.xilinx.com/r/en-US/ug1089-kv260-starter-kit/Ethernet-Recovery-Tool) for loading the on-board Xilinx Image Recovery Tool.
5. Upload the desired binary file (e.g. 'Infinite-ISP_v1.0-1080p.bin') on the Kria KV260 AI Starter Kit.
6. Reset the Kria KV260 board and visualize the Infinite-ISP output on your monitor screen.
7. Connect the USB cable with the JTAG/USB port on Kria to read the messages over UART.
8. You can remove the SD card from the Kria board, extract the dumped single RGB-RAW pair and 300 RGB frames (if applicable) and visualize them using the provided scripts.

## Contact
For any inquiries or feedback feel free to reach out.

Email: isp@10xengineers.ai

Website: http://www.10xEngineers.ai

LinkedIn: https://www.linkedin.com/company/10x-engineers/
