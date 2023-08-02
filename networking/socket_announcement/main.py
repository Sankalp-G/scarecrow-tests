PORT = 50000
MAGIC = "fna349fn"

from time import sleep
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST, gethostbyname, gethostname

s = socket(AF_INET, SOCK_DGRAM) # create UDP socket
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) # this is a broadcast socket
my_ip = gethostbyname(gethostname())

while 1:
    data = str.encode(MAGIC+"hello world")
    s.sendto(data, ('<broadcast>', PORT))
    print("sent service announcement")
    sleep(5)
