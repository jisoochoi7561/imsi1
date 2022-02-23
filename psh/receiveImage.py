#!/usr/bin/env python3
import serial
import time
import base64

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    ser.reset_output_buffer()
#    ser.set_buffer_size(rx_size = 12800, tx_size = 12800)
    
    sb = b''
    fh = open("imageToSave.jpeg", "wb")

    while True:
        if ser.in_waiting > 0:
            line = ser.readline()
            if line == b'EndOfPacket':
                print(line)
                print(sb)
                fh.write(base64.b64decode(sb))
                fh.close()
                break

            sb += line
#            fh.write(line)
#            time.sleep(0.11)
#            line = ser.readline().decode('utf-8').rstrip()
            print(line)
        
