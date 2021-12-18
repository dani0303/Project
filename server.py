import socket
import threading

PORT = 5050
SEVER = "10.23.104.78"
ADDR = (SERVER, PORT)

##gets the host from the the server's ip address
SEVER = socket.gethostname(socket.gethostname())

##streams data 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handler(conn, addr):
    print("[NEW CONNECTION] {addr} connected. ")
    connected = True
    while connected:
        msg = conn.recv()

def start():
    server.listen()
    while True:
       conn, addr =  server.accept()
       thread = threading.Thread(target=handler, args=(conn, addr))
       thread.start()
       print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")


print("STARTING")

start()

