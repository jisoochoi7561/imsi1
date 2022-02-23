import picamera
import time
from datetime import datetime

timeDelay = 0 # 몇 초 뒤에 사진을 찍을 것인지
now = datetime.now()

camera = picamera.PiCamera()
camera.resolution = (2592, 1944)

def takePicture():
    if (detectSound()): # 소리가 감지되면 일정 시간 뒤에 사진 촬영
        time.sleep(timeDelay)
        camera.capture('%d.%d.%d.%d.%d.%d.jpg' %(now.year, now.month, now.day, now.hour, now.minute, now.second))
        print("촬영 완료")

def detectSound():
    return True

def main():
    time.sleep(1) # 실행 시 초기에 카메라 세팅 시간
    takePicture()

if __name__ == "__main__":
    main()
