from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import sys

client_name = "Viraat"

s = xmlrpc.client.ServerProxy("http://127.0.0.1:2347/")
print(s.is_even(4))
print(s.is_even(19))


print("Program uses" + "\n" + "Localhost: 127.0.0.1:2347" +"\n"+ "Port Number: 2347")

print(s.connected_clients(client_name))

client_message = input("Enter message for Server:")
print(s.talk_toeach(client_message))

list_files = input("Do you wanna list the files present in Sever? (0- no; 1- yes)")

if(list_files == '0'):
    print("Program aborted!; Goodbye!!")
    sys.exit()

file_list = []
file_list = s.list_clientfiles()
print("FILES AVAILABLE AT SERVER:")

for i in file_list:
    print(i)

display_file = input("Enter the file you wish to read:")

if display_file.strip() in file_list:
    print("File present in Server; will start read now")
else:
    print("Please enter a file name from the above list; Goodbye!!")
    sys.exit()

print("FILE DATA FROM SERVER")
print(s.readfile_client(display_file))