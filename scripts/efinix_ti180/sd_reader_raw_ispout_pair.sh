#!/bin/bash

## Always run this script with sudo privileges

## ISPout Image type
RAW=0
RGB=1
YUV=2

TYPE=1      ##change this to select type of image in SD card 


## Image information - RAW & ISPout
RAW_WIDTH=1952
RAW_HEIGHT=1112
ISPOUT_WIDTH=1920
ISPOUT_HEIGHT=1080

## Frame information in SD Card
BLOCK_SIZE=512
RAW_FRAME_ADDR="$((512*20))"
RAW_FRAME_BLOCKS="$((($RAW_WIDTH * $RAW_HEIGHT * 4) / $BLOCK_SIZE))"		
ISPOUT_FRAME_ADDR="$(($RAW_FRAME_ADDR + $RAW_FRAME_BLOCKS + $RAW_FRAME_ADDR))"
ISPOUT_FRAME_BLOCKS="$((($ISPOUT_WIDTH*$ISPOUT_HEIGHT*4) / $BLOCK_SIZE))"



RAW_BITS=10
RAW_BAYER='RGGB'
if [ $TYPE == $RGB ]
then
    BITS=8
    CSPACE=RGB
elif [ $TYPE == $YUV ]
then
    BITS=8
    CSPACE=YUV
fi
NAME='TestImage'

## SD Card Information

# SD file name. Carefully confirm your sd card device from /dev/ directory. It will be of format sdX
sd_file='/dev/sdf'

# Name of the file where SD card contents will be written to
out_file_raw='RAW_'$NAME'_'$RAW_WIDTH'x'$RAW_HEIGHT'_'$RAW_BITS'bits_'$RAW_BAYER'.bin'
if [ $TYPE == $RGB ]
then
    out_file_ispout='RGB_'$NAME'_'$ISPOUT_WIDTH'x'$ISPOUT_HEIGHT'_'$BITS'bits_'$CSPACE'.bin'
elif [ $TYPE == $YUV ]
then
    out_file_ispout='YUV_'$NAME'_'$ISPOUT_WIDTH'x'$ISPOUT_HEIGHT'_'$BITS'bits_'$CSPACE'.bin'
fi
# Number of blocks (each of size 512 Bytes) to be read from SD card and written to $out_file.
# It corresponds to the size of RAW/ISPout image in unit of blocks (512 Bytes).
number_of_blocks_raw="$((($RAW_WIDTH * $RAW_HEIGHT * 4)/512))"
number_of_blocks_ispout="$((($ISPOUT_WIDTH * $ISPOUT_HEIGHT * 4)/512))"

## Command Execution

# Execute dd command to read the sectors from SD card and write them to the $out_file
dd if="$sd_file" of="./$out_file_raw" bs=512 count="$number_of_blocks_raw" skip=$RAW_FRAME_ADDR
dd if="$sd_file" of="./$out_file_ispout" bs=512 count="$number_of_blocks_ispout" skip=$ISPOUT_FRAME_ADDR

