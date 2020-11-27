import socket
import sys

def RoboDK2KUKA():
    #Get Host + Port for RoboDK
    host = socket.gethostname()
    port = 5000

    DK_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    DK_socket.bind((host,port))
    DK_socket.listen(2) 

    connection, client_add = DK_socket.accept()
    print("Connection From: ", str(client_add))

    #KUKA_socket = socket.socket()
    #KUKA_socket.connect(('172.31.1.147',7000))

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = connection.recv(2048).decode()
        if not data:
            # if data is not received break
            break
        print("RoboDK Data: \n", data)
        #KUKA_socket.sendall(data.encode())
  # send data to the client
    print("it broke")

def main():
    RoboDK2KUKA()

main()