# USER GUIDE

The Infinite-ISP Configuration Menu contains three options. You can change sensor configurations such as exposure duration and analog/digital gain settings, start burst capture of up to 193 consecutive frames, change ISP parameters and even adjust the focus of the sensor module. The hierarchy of the Infinite-ISP Configuration Menu is as follows:

<kbd>![status before dumping](/doc/user_guide/user_menu_top.png)</kbd> 


## Change Sensor Configuration:


Upon selecting option 1 of the “Infinite-ISP Configuration Menu”, you will be asked to change either the sensor’s exposure duration or the sensor’s analog/digital gains. The hierarchy of the “Change Sensor Configuration” menu is shown below.

<kbd>![status before dumping](/doc/user_guide/user_menu_sensor.png)</kbd> 


Upon selecting option 1 (Change Sensor Exposure) of the “Change Sensor Configuration” menu, you will be shown the current “coarse_integration_time” register value and you will be asked to give exposure duration in the units of lines_of_frame (time required by sensor clock to process one line of the frame). Upon entering any value, the exposure duration of the sensor will change. This change can be observed live on the HDMI display attached to the board.

Upon selecting option 2 (Change Sensor Gain) of the “Change Sensor Configuration” menu, you will be shown the value of the current gain values and you will be asked to modify the value of any gain register. In options 1 – 4, you will be shown the current gain register value of that particular option and you will be prompted for the new value. In option 5, the default sensor gains will be applied. In option 6, the current register values of gain registers will be displayed. In option 7, you will go back to the “Change Sensor Configuration” menu. The hierarchy of the “Change Sensor Gain” menu is shown below.

<kbd>![status before dumping](/doc/user_guide/sensor_gain.png)</kbd>


Upon selecting option 3 (Exit)  of the “Change Sensor Configuration” menu, the current exposure and gain register values will be written to “ExpAndGain_AR1335.txt” or “ExpAndGain_OV5647.txt” file in the SD card and then you will go back to the “Infinite-ISP Configuration Menu”. In case you don’t have an SD card inserted in the board, it will wait for a few seconds and will give an error message.


## Start Burst Capture:

 
Upon selecting option 2 (Start Burst Capture) of the “Infinite-ISP Configuration Menu”, you will be asked to enter the number of frames you want to dump. Then you will be asked to enter the number of frames you want to skip at the start of the burst capture feature. As soon as you insert the value, the feature will start and will wait for the frames you entered to be skipped. During this period, it will show you the time at which the scene will be captured and the time passed since your input. In case of AR1335, the Frames Per Second (FPS) are 30 and if the value you entered is 100, it will wait for floor(100 / FPS) i.e. floor(100 / 30) = 3 seconds and then it will capture the scene.

Once the wait period is over, it will show you the status of the burst capture feature. The ‘In memory’ flag rises once the scene is captured and the ‘In SD card’ flag rises once the captured frames are successfully written to the SD Card. It first writes the RAW frames and then the ISPout frames. Once the frames get dumped into the SD card, it will bring you back to the “Infinite-ISP Configuration Menu”.


## Configure ISP Parameters:


There are several ISP modules that can be configured through the “Configure ISP Parameters” menu option. Go through them and play with the Infinite-ISP by changing the parameters of different modules. Each sub-module will give you its current parameter values and will prompt you for the new values.


## Change VCM Position:


You can change the focus of the AR1335 sensor module by changing the VCM position register value. It will give you the current register value and will ask for the new position register value. This feature requires a board modification to work properly. For further information, contact us at https://10xengineers.ai

