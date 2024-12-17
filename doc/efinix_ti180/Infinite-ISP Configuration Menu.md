# USER GUIDE

The Infinite-ISP Configuration Menu contains four options. You can change sensor configurations such as exposure duration and analog/digital gain settings, change ISP parameters, start RAW10/RGB pair capture, and enable auto exposure firmware loop. The hierarchy of the Infinite-ISP Configuration Menu is as follows:

<kbd>![status before dumping](/doc/user_guide/Efinix_User_Menu_top.png)</kbd> 


## Change Sensor Configuration:


Upon selecting option 1 of the “Infinite-ISP Configuration Menu”, you will be asked to change either the sensor’s exposure duration or the sensor’s analog/digital gains. The hierarchy of the “Change Sensor Configuration” menu is shown below.

<kbd>![status before dumping](/doc/user_guide/Efinix_User_menu_sensor.png)</kbd> 


Upon selecting option 1 (Change Sensor Exposure) of the “Change Sensor Configuration” menu, you will be shown the current “coarse_integration_time” register value and you will be asked to give exposure duration in the units of lines_of_frame (time required by sensor clock to process one line of the frame). Upon entering any value, the exposure duration of the sensor will change. This change can be observed live on the HDMI display attached to the board.

Upon selecting option 2 (Change Sensor Gain) of the “Change Sensor Configuration” menu, you will be shown the value of the current gain values and you will be asked to modify the value of any gain register. In options 1 – 3, you will be shown the current gain register value of that particular option and you will be prompted for the new value. In option 4, the default sensor gains will be applied. In option 5, the current register values of gain registers will be displayed. In option 6, you will go back to the “Change Sensor Configuration” menu.


## Configure ISP Parameters:


There are several ISP modules that can be configured through the “Configure ISP Parameters” menu option. Go through them and play with the Infinite-ISP by changing the parameters of different modules. Each sub-module will give you its current parameter values and will prompt you for the new values.


## Capture RAW10/RGB Pair:

 
Upon selecting option 3 (Capture RAW10/RGB Pair) of the “Infinite-ISP Configuration Menu”. The RAW10/RGB pair capturing will start. Once the wait period is over, it will show you the status of the capture pair. It first writes the RAW10 frame and then the ISPout frame. Once the frame pair get dumped into the SD card, it will bring you back to the “Infinite-ISP Configuration Menu”.


## AE Firmware Loop

Upon selecting option 4 of the “Infinite-ISP Configuration Menu”, you will be asked to change the auto exposure loop. Option 1 for AE firmware loop and option 2 for Hardware AE.
