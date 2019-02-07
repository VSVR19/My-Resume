import socket
import sys
from _thread import *
import os

HOST = '127.0.0.1'
PORT = 2346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Socket Created!")

try:
	s.bind((HOST, PORT))
except socket.error:
	print(socket.error)
	print("Socket bind failed!")
	sys.exit()
print("Socket bind complete!")

s.listen(19)
print("Socket listening")

def clientthread(conn):
	while True:
		try:
			data = conn.recv(2346)
		except ConnectionResetError:
			print("Connection Closed by client; Goodbye!")

		
