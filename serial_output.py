import serial
import time

sr = serial.Serial('/dev/ttyUSB1', 9600, timeout = 1)

############ 루프 시작 ##############

while True :
    # line = sr.readline().decode("utf-8")
    # print(line)
    msg = "2,5 6 4 5 6 0,10 35 20 34 28 0,1 1 0 1 1 0"
    # msg = "3 5 7\n40 50 20\ntrue true false"
    # msg = '34 ,22'
    sr.write(msg.encode())
    time.sleep(100)