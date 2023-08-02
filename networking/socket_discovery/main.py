PORT = 50000
MAGIC = "fna349fn"

from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM) # create UDP socket
s.bind(('', PORT)) # bind to all interfaces on port 50000

while True:
    data, addr = s.recvfrom(1024) # wait for a packet
    if data.startswith(str.encode(MAGIC)):
        print("got service announcement from", addr[0], ' ', data[len(MAGIC):])
