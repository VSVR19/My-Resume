from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
#from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpc.client
import os

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
        # str_files_present = ','.join(files_present)
        # list_files_present = str_files_present.split(',')

        # neat_list = [' {0} '.format(elem) for elem in list_files_present]

        # for i in range(len(neat_list)):
            # print(neat_list[i])
        

        # print(files_present)
        return files_present

    def sendfile_client():
        print("sendfile_client method")
        return "sendfile_client method"
        

    server = SimpleXMLRPCServer(("127.0.0.1", 2347))
    print("Listening on port 2347...")
    server.register_function(is_even, "is_even")
    server.register_function(connected_clients, "connected_clients")

    server.register_function(talk_toeach, "talk_toeach")
    server.register_function(list_clientfiles, "list_clientfiles")

    server.serve_forever()
    
except:
    print("Error logs caught by exception handlers")