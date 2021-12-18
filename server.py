import socket
import threading

"""
HOW SOCKETS WORK:
    1. declare your ip address where you will be running a server and port
    2. bind the ip address to a socket where it will stream the server
    3. create a handler function where it will store messages recivied from the clients
        (this operation will be done using threading which hold multiple connections at once
        and so it doesn't keep other possible connections from waiting)
    4. create a method to have the server listen for incoming connections

    author(Daniel Rodriguez)
    source(Tech with Tim)
    date(12/18/21)
"""

#specifies the length of the message sent to the server and this cannot change
HEADER = 64
PORT = 5050
#gets our computer's ip address to host our server
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "192.168.4.106"
#binds server and port to socket
ADDR = (SERVER, PORT)
#begins to stream data through the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#BINDS
server.bind(ADDR)
#format used to convert bytes into strings
FORMAT = 'utf-8'
#message that will printed the console when there disconnections
DISCONNECT_MSG = "disconnect"

def handler(connm, addr):
    #will print who is connected to the server
    print(f"[NEW CONNECTIONS] {addr} connected.")
    connected = True
    #will wait for a message sent to the server
    while connected:
        #will store the message in msg in form of bytes then decode it into a string using utf-8
        msg_len = conn.recv(HEADER).decode(FORMAT)
        #store message into int before being decoded
        msg_len = int(msg_len)
        #finally decodes message sent to the server
        msg = conn.recv(msg_len).decode(FORMAT)
        #prints the message and the address
        if msg == DISCONNECT_MSG:
            connected = False
        print(f"[{addr}] {msg}")
    conn.close()

def start():
    #begins to listen for connections that are connected to the server
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    #keeps program listening for connections until we tell it to stop
    while True:
        #this line of code will wait for connection and then store the port and ip addres in variables (CONN, ADDR)
        conn, addr = server.accept()
        #passes connection information to handler
        thread = threading.Thread(target=handler, args=(conn, addr))
        #starts the threading process
        thread.start()
        #this line will represent the amount of threads (aka clients) connected and print them
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[SERVER] is starting")
start()
