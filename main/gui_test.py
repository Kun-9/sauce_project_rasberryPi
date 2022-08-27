import tkinter
import socket
from source_management import sauce_manage
import serial
import time
from tkinter import *
from tkinter import messagebox
import threading
# from socketClass import serverModule

global gloStr
gloStr = ''

global serialArdu
serialArdu = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)

global arr
arr = [[0 for col in range(4)] for row in range(6)]

s = sauce_manage.sauceList()

s.addsauce("hello", 1, 2277814929)
s.addsauce("hello2", 1, 21124312446)






class SokServer:
    
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        
    def startServer(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        # 포트 사용중이라 연결할 수 없다는 
        # WinError 10048 에러 해결를 위해 필요합니다. 
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


        # bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됩니다.
        # HOST는 hostname, ip address, 빈 문자열 ""이 될 수 있습니다.
        # 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용합니다. 
        # PORT는 1-65535 사이의 숫자를 사용할 수 있습니다.  
        server_socket.bind((self.HOST, self.PORT))

        # 서버가 클라이언트의 접속을 허용하도록 합니다. 
        server_socket.listen()

        # accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다. 
        client_socket, addr = server_socket.accept()

        # 접속한 클라이언트의 주소입니다.
        print('Connected by', addr)


        # 무한루프를 돌면서 
        while True:

            # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다. 
            data = client_socket.recv(1024)

            # 빈 문자열을 수신하면 루프를 중지합니다. 
            if not data:
                break


            # 수신받은 문자열을 출력합니다.
            print('Received from', addr, data.decode())
            
            global gloStr
            gloStr = data.decode()
            
            # 아두이노에 문자열 전송
            serialArdu.write(data)
            print('gloStr = ',gloStr)
            
                
            # 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코) 
            client_socket.sendall(data)


        # 소켓을 닫습니다.
        client_socket.close()
        server_socket.close()


class SerialInput:
    def __init__(self) -> None:
        pass    
    
    def readSerial(self):
        while 1:
            if serialArdu.in_waiting != 0:
                content = serialArdu.readline().decode()
                
                stringType = content[0:1]
                if (stringType == '1') :
                    for i in range(6):
                        # if serialArdu.in_waiting != 0:
                        id = serialArdu.readline().decode()[0:-3].replace(" ", "")
                        
                        if int(id[:2]) != 0:
                            if s.findById(int(id)):
                                print("이미 등록된 ID : ", int(id))
                            else :
                                s.addsauce('null', 1, int(id))
                                print("새로 등록한 ID : ", int(id))
                            
                    
                else :
                    
                    print(content, end="") 
                


# global threadNumber


def server():
    a = SokServer('192.168.0.17',8080)    
    a.startServer()

def inputString():
    str = SerialInput()
    str.readSerial()

def tempThread():   
    for i in range(100):
        print(i)
        time.sleep(1)
    
    
    
ServerThread = threading.Thread(target=server)
InputThread = threading.Thread(target=inputString)

ServerThread.start()
InputThread.start()
# # print(len(s.getsauceList()))
# print(s.getsauceList()[0].getId())
# print(s.getsauceList()[1].getId())

   

        
    
    

