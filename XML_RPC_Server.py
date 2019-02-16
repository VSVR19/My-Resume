from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import os
import sys

try:
    def is_even(num):
        return num % 2 == 0

    
    def connected_clients(client_name):
        print("Connected with client " + client_name)
        return "Connected with server as " + client_name

    def talk_toeach(client_message):
        print("Message from client: " + client_message)
        return "Server says Hi!"

    def list_clientfiles():
        files_present = os.listdir("C:\\Users\\Venkat\\Desktop\\Team_3_A02_submission")
        
        return files_present

    def readfile_client(display_file):
        file_open = open("C:\\Users\\Venkat\\Desktop\\Team_3_A02_submission\\" + display_file)
        file_content = file_open.read()

        return file_content        
        

    server = SimpleXMLRPCServer(("127.0.0.1", 2347))
    print("Listening on port 2347...")
    server.register_function(is_even, "is_even")
    server.register_function(connected_clients, "connected_clients")

    server.register_function(talk_toeach, "talk_toeach")
    server.register_function(list_clientfiles, "list_clientfiles")
    server.register_function(readfile_client, "readfile_client")

    server.serve_forever()
    
except:
    print("Error logs caught by exception handlers")