#!/bin/bash

#(python3 test.py &) | while read -r line; 
(python3 sound.py) | while read -r line; 
do
  if [ $line -eq 1 ]; then
	echo "$line"
	echo "1234"
#	python3 sendCaptureSignal.py
#	python3 imageReceiving.py

#    #pkill -f test.py
  else
    echo "$line"
  fi
#	echo "1"
done

#python3 sendCaptureSignal.py
#python3 imageReceiving.py
