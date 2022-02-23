#!/usr/bin/env python3
import serial
import time

#def cmdCapture() :
#    ser.write(b"capture\n")
#    line = ser.readline().decode('utf-8').rstrip()
#    print(line)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    while True:
    #for i in range(1000):
        #time.sleep(1.8)
        ser.write(b"CaptureImage")
        ser.flush()

        #line = ser.readline().decode('utf-8').rstrip()
        #print(line)
#    cmdCapture()

