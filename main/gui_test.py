import socket
# from sauceManagement import sauce_manage
from sauceManagement import sauce_manage_j
import serial
import time
import threading
import json as j

global gloStr
gloStr = ''
global check

global serialArdu
serialArdu = serial.Serial('/dev/ttyUSB_DEV1', 9600, timeout = 1)

global arr
arr = [[0 for col in range(4)] for row in range(6)]

s = sauce_manage_j.sauceList()

# s.addsauce("hello", 1, 2277814929)
# s.addsauce("hello2", 1, 21124312446)

global client_socket

check = 0





class SokServer:
    
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        
    def startServer(self):
        while 1:
            
            global client_socket
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
            acp = server_socket.accept()
            client_socket = acp[0]
            addr = acp[1]
            # 접속한 클라이언트의 주소입니다.
            print('Connected by', addr)
            
            global check
            check = 0

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
                
                # 임시로 7로 설정
                # 7이 들어왔을때 소스 수정
                # 들어오는건 json 형식의 소스 정보와 아이디
                # ex) {"name" : "간장", "isLiquid" : "1", "id" : "123456"}
                
                if gloStr[:1] == '7':
                    editJson = j.loads(gloStr[1:])
                    
                    print('editJson : ' + str(editJson))
                    
                    id = editJson["id"]
                    s.editSauce(id, editJson)
                    
                    # 스캔 시작
                    # serialArdu.write("0".encode())
                    
                else:
                    # 아두이노에 문자열 전송
                    serialArdu.write(data)
                    print('gloStr = ',gloStr)
                    
                    # 원래 1~6 으로 시작함 
                    # 0으로 들어오면 소스 스캔 시작함
                    # 결과는 어떻게 내보내지?
                    # dataType
                    # 0 : 일반 메시지
                    # 1 : 소스 출력 문자열
                    # 2 : 소스 변경 문자열
                    # 3 : 
                    # 문자열의 가장 앞 문자가 2라면 소스 수정 메서드 실행
                    # 파싱 후 이름, 액체여부 값 파악
                    # if int()
                    
                    # sauce = s.getSauce(id)
                    # sauce.setName()
                    # sauce.setLiquid()    
                
                    
                # 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코) 
                # client_socket.sendall("client".encode())
                # client_socket.send("string".decode())
                # client_socket.sendall(data)


            # 소켓을 닫습니다.
            # client_socket.close()
            # server_socket.close()

            


class SerialInput:
    def __init__(self) -> None:
        pass    
    
    def readSerial(self):
        while 1:
            if serialArdu.in_waiting != 0:
                content = serialArdu.readline().decode()
                
                stringType = content[0:1]
                # 메시지 타입이 1이라면 소스 스캔값 받아옴
                # 일반 문자열은 0
                if (stringType == '1') :
                    for i in range(6):
                        # if serialArdu.in_waiting != 0:
                        id = serialArdu.readline().decode()[0:-3].replace(" ", "")
                        
                        if int(id[:2]) != 0:
                            s.registCurrentSauce(i, str(id))
                            
                        else :
                            # data = {"name" : 'name', "isLiquid" : 1, "id" : 'null'}
                            s.registCurrentSauce(i, 0)
                            
                    s.saveCurrnetSourceList()
                    sendStr = str(s.getCurrentsauceList()).replace('\'', '\"' )
                    client_socket.sendall(sendStr.encode())
                    # print(s.getCurrentsauceList())
                    print('서버에 저장되어있는 객체 배열 : ' + sendStr)
                else :
                    
                    print(content, end="") 
                    # [2:]
                


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

    
while True:
    if check == 1:
        check = 0
        ServerThread.join()
        ServerThread.start()
        

def connect(self, ip, port):
    retryCount = 0
    retry = True
    while(retry):
        try:
            print ('Connect Server')
            self.socket.connect( (str(ip), int(port)) )
            retry = False
            return 1
        except:
            print ('Fail')
            print ('retry after ')
            retry = True
            
print( "connection lost... reconnecting" )
connected = False  
#recreate socket
clientSocket = socket.socket()  
while not connected:     
    #attempt to reconnect, otherwise sleep for 2 seconds     
    try:         
        clientSocket.connect( ( host, port ) )         
        connected = True         
        print( "re-connection successful" )     
    except socket.error:         
        sleep( 2 )  
        #continue normal operations 

        
    

