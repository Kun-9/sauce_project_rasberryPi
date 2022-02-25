from time import time
import serial
import time
# import pyfirmata

# board = pyfirmata.Arduino('/dev/ttyUSB0')



###########     SETUP   ##############

LED_pin = 2
port = "/dev/ttyUSB0"
SER = serial.Serial(port, 9600)
SER.flushInput()
# GPIO.setup(LED_pin, GPIO.OUT)

######################################

###########     loop    ##############


while True:
    # msg = 'hello'
    # SER.write(msg.encode())
    # time.sleep(1000)
    
    LINE = bytearray()

    for c in SER.read():
        LINE.append(c)
        byte_line = bytes(LINE)

        if byte_line.find(b'abcd') != -1:
            str_decoded = byte_line.decode('ascii')
            LINE.clear()
            SER.flushInput()
            
    # print(board)
    # GPIO.output(LED_pin, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(LED_pin, GPIO.LOW)
    # time.sleep(1)

######################################


