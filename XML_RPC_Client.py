from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://127.0.0.1:2347/")
print(s.is_even(4))
print(s.is_even(19))
	
print(s.connected_clients())