import socket
import sys

def KUKA2RoboDK():
    # Get the Host + Port for KUKA
    host = '10.30.79.179'
    #host = '172.31.1.147'
    port = 7000

    KUKA_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Get Socket Instantiated
    KUKA_socket.connect((host,port))

    # Tell user Connected to KUKA
    
    print("Connection From: ", KUKA_socket.getsockname())

    # Once connected to KUKA, Connect to RoboDK's Input
    RoboDK_socket = socket.socket()
    RoboDK_socket.connect(('172.31.1.149', 5000))

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = KUKA_socket.recv(2048).decode()
        if not data:
            # if data is not received break
            break
        print("KUKA Data: \n")
        RoboDK_socket.sendall(data.encode())  # send data to the client

    # close the connection

def main():
    KUKA2RoboDK()

main()