import socket
import sys


def serverside():

    #Defines the socket that allows --> RoboDK PC <-> TCP 
    hostname = socket.gethostname() # Grabs local host name
    port = 7000 # Placeholder number to go in RoboDK interface, can be anything above 1024 and not in use afaik
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((hostname,port))
    sock.listen(2) # wait for connections

    
    #Waits for the RoboDK PC to connect to the TCP Server
    connection, client_add = sock.accept()

    #if forwarding via the Server, below creates the socket --> TCP <-> KUKA robot
    sockRobot = socket.socket()
    #Ip of my KUKA robot and Port open on the robot
    sockRobot.connect(('172.31.1.147', 7000))

    print("Connection From: ", str(client_add))
    pack_data = "initial"
    retdata = "initial"
    while True: 
        #GetRoboDK Data
        pack_data = connection.recv(2048).decode()
        print(pack_data)
        if not pack_data.strip():
            print("packet empty")
        #Extruder Commands to go to external logic board to control extruder
        elif "Extrude" in pack_data:
            print("\nExtrude Command Found:\n", pack_data)

        elif not "Extrude" in pack_data:
            print("\nCommand Found:\n", pack_data)
            #Send data from TCP to robot
            
            sockRobot.sendall(pack_data.encode())

        #Get data back from robot
        retdata = sockRobot.recv(2048).decode()

            if not retdata.strip():
                break
            print("Data back from robot (handshake): ", retdata)
            #forward data on from TCP to RoboDK
            connection.sendall(retdata.encode())  
        else:
            print("we done fucked up")
    print("Found Empty Packet")
 
    connection.close()
def main():
    serverside()

main()
