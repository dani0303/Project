import socket
import sys
import getopt
import threading
import subprocess

#Global VARS
listen = False
command = False
upload = False
execute = ""
target = ""
upload_des = ""
port = 0

#Handle Commands
def usage():
    print("BHP tool")
    print("Usage: bhpnet.py -t target_host -p port")
    print("-l --listen  -listen on [host]:[port] for incoming connections")
    print("-e --execute=file_to_run  -execute the given file upon receiving a connection")
    print("-c --command  -initialize a command shell")
    print("-u --upload=destination  -upon receiving connection upload a file and write to [destination]\n")
    print("Examples: \n")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=/user/home/target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    sys.exit(0)

def main():
    global listen
    global command
    global upload
    global target
    global upload_des

    if not len(sys.argv[1:]):
        usage()
    #Reade options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu", ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    if not listen and len(target) and port > 0:
        #read buffer from commandline
        #this will block, so send CTRL-D if not sending input
        #to stdin
        buffer = sys.stdin.read()
        client_sender(buffer)
    """
    we are going to listen and potentailly
    upload things, execute commands, and drop a shell back
    depending on our current command line options
    """
    if listen:
        sever_loop()

def client_sender(buffer):
    #Make a socket and start streaming
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
