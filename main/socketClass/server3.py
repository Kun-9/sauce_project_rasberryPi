from asyncio.windows_events import NULL
import socket
import time

host = '192.168.0.17' # 호스트 ip를 적어주세요
port = 8080            # 포트번호를 임의로 설정해주세요

server_sock = socket.socket(socket.AF_INET)
server_sock.bind((host, port))
server_sock.listen(1)
print("기다리는 중..")
out_data = int(10)

while True: #안드로이드에서 연결 버튼 누를 때까지 기다림
    client_sock, addr = server_sock.accept() # 연결 승인

    if client_sock: #client_sock 가 null 값이 아니라면 (연결 승인 되었다면)
        print('Connect : ', addr) #연결주소 print
        
        while(True) :
            in_data = client_sock.recv(1024)
            
            # in_data = client_sock.recv(1024) #안드로이드에서 "refresh" 전송
            print('rcv :', in_data.decode()) #전송 받은값 디코딩
            
        
        
        # while in_data : #2초마다 안드로이드에 값을 전달함 (추후 , STOP , Connect 옵션 설정 가능)
        #     client_sock.send(str(out_data).encode("utf-8")) # int 값을 string 으로 인코딩해서 전송, byte 로 전송하면 복잡함
        #     print('send :', out_data)
        #     out_data = out_data+1 #전송값 +1
        #     time.sleep(2)

client_sock.close()
server_sock.close()