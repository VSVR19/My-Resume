from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

client_count = 0

try:
	def is_even(num):
		return num % 2 == 0

	def connected_clients():
		global client_count
		client_count = client_count + 1
		print("Connected with client number " + str(client_count))
		return "Connected with client number " + str(client_count)

	def client_message():
		return("Hi from Server")

	server = SimpleXMLRPCServer(("127.0.0.1", 2347))
	print("Listening on port 2347...")

	server.register_function(is_even, "is_even")
	server.register_function(connected_clients, "connected_clients")
	server.register_function(client_message, "client_message")
	
	server.serve_forever()

except:
	print("Error logs caught by exception handlers")