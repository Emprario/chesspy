#!/usr/bin/env python3
import socket
from time import sleep
hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))

socket.send(b"Hey my name is Olivier!")
socket.send(b"EOF")

print("Close")
socket.close()