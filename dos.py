import sys
from scapy.all import *

if len(sys.argv) != 3:
    print "Usage: ./handshake.py <target-ip> <source-port>"
    sys.exit(1)

target = sys.argv[1]
sp = int(sys.argv[2])

i = IP()
i.dst = target
print "IP layer prepared: ", i.summary()

t = TCP()
t.dport = 80
t.sport = sp
t.flags = "S"
print "Sending TCP SYN Packet: ", t.summary()
ans = sr1(i/t)
print "Reply was: ",ans.summary()

t.seq = ans.ack
t.ack = ans.seq + 1
t.flags = "A"
print "Sending TCP ACK Packet: ", t.summary()
ans = sr(i/t/"X")
