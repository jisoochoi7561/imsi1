#!/usr/bin/env python3
import base64
import serial
import time

with open("linux-bsd.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
#    print(str)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    
#    print(str)
    j = 0
    while True:
        time.sleep(1.8)
        if str[j:j+255] == b'': #   stop condition
            ser.write(b'EndOfImageTransmission')
            break;
        print(str[j:j+255])     #   maximum payload size : 255
        ser.write(str[j:j+255])
        j = j + 255
        ser.flush()
#        time.sleep(1)
