"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).
"""
import time
import socket
import base64

hostMACAddress = 'E4:5F:01:6A:57:BD' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 1 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 1024
while 1:
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.bind((hostMACAddress,port))
    s.listen(backlog)
    try:
        client, address = s.accept()

        #sb = b''
        #fh = open("image.jpeg", "wb")

        #while 1:
        #    data = client.recv(size)
        #    if data:
        #        print(data)

         #       if data[len(data)-3::] == b'EOF':
         #           fh.write(base64.b64decode(sb))
          #          fh.close()
           #         print("Image Received, closing socket")	
            #        client.close()
             #       s.close()
              #      exit(0)
                    #break

               # sb += data
        #client.send(data)
        #while 1:
        data = b"hi"
        while True:
            client.send(data)
            time.sleep(1)
        print(data)
    except:	
        print("Closing socket")	
        client.close()
        s.close()
        exit(1)
