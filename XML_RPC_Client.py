from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

client_name = "Viraat"
# client_message = "HHM!"

s = xmlrpc.client.ServerProxy("http://127.0.0.1:2347/")
print(s.is_even(4))
print(s.is_even(19))

print(s.connected_clients(client_name))

client_message = input("Enter message for Server:")
print(s.talk_toeach(client_message))

list_files = input("Do you wanna list the files present in Sever? (0- no; 1- yes)")
# print(s.list_clientfiles())
file_list = []
file_list = s.list_clientfiles()
print("FILES AVAILABLE AT SERVER:")

for i in file_list:
    print(i)