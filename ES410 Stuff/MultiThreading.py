import socket
import os
from _thread import start_new_thread

ServerSideSocket = socket.socket()
#flat:
host = '10.30.79.149'
#uni: 
#host = '172.31.1.150'
port = 5000
ThreadCount = 0


try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))


print('Socket is listening..')
ServerSideSocket.listen(1)


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        pack_data = connection.recv(2048).decode()
        response = 'Server message: ' + pack_data
        if not pack_data:
            break
        elif "Extrude" in pack_data:
            #Extrude dont send to robot
            print("hi")
        else:
            connection.sendall(response.encode())

    connection.close()



while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + str(address))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()