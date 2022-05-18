import threading, time
import socket as s

PORT = 1337

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.bind(('127.0.0.1', PORT))
socket.listen(1)
print('[+] Servidor escuchando en el puerto:', PORT)

def recvData():
    while True:
        print('\n'+'client>', sc.recv(1024).decode())

def sendData():
    while True:
        msg = input().encode('utf-8')
        sc.send(msg)

def handleConnection():
    recvDataThread = threading.Thread(target=recvData)
    recvDataThread.start()
    sendData()

print('[+] Esperando conexión de cliente...')
sc, addr = socket.accept()
print('[+] Cliente conectado desde:', addr)

handleConnection()
