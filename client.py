import threading, time
import socket as s

IP = input('HOST (def: loop): ') or '127.0.0.1'
PORT = int(input('PORT (def: 1337): ') or 1337)
socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    
def recvData():
    while True:
        print('\n'+'server>', socket.recv(1024).decode())

def sendData():
    while True:
        msg = input().encode('utf-8')
        socket.send(msg)

def handleConnection():
    recvDataThread = threading.Thread(target=recvData)
    recvDataThread.start()
    sendData()
    
print('[*] Conectando...')
try:
    socket.connect((IP, PORT))
    print('[+] Conexión exitosa')
    handleConnection()
except:
    print('[-] No ha sido posible conectarse')
