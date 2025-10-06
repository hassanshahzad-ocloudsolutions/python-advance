#Sockets and Network Programming

'''
Network programming means writing code that allows computers (or programs) to communicate over a network — 
such as the Internet or a local network (LAN).

A socket is like a two-way communication endpoint —
it is where data is sent from and to between computers.

required: IP address, port number, socket(combination of ip address and port number)

TCP(Connection oriented) and UDP(Not Connectuin Oriented)
'''

import socket
#AF_INET means internet socket. Other sockets are also available like UNIX socket
#SOCK_STREAM means TCP. Other are also available like UDP(SOCK_DGRAM)

#Created Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1' , 5555))
s.listen()

while True:
    client, address = s.accept()
    print(f'Connected to {address}')
    client.send("You are connected".encode()) 
    client.close()