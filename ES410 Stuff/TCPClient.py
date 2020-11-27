import socket
import sys

# cd *\Desktop\PythonAdventures\Programs\ python TCPClient.py

def client_program():
    host = socket.gethostname()  
    port = 5000 
    client_socket = socket.socket()  
    client_socket.connect((host, port))  

    message = input(" -> ")  

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  
        

        print(data)  

        message = input(" -> ")  

    client_socket.close() 


def main():
    client_program()

main()