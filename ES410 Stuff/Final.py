# Commands for running program in CMD
#ProgramPath, RoboDK_IP, RoboDK_Port, Kuka_IP, Kuka_Port = sys.argv

# in CMD python Final.py "RoboDK IP" "RoboDK Port" "KUKA IP" "KUKA Port"

import asyncio
import serial
import sys

# Create serial port on port that Sammy is connected to, check this in command line
Serial_Port = serial.Serial('COM3')

# Manual defining Info if not using command line to send this information

RoboDK_IP = '172.31.1.149'    # RoboDK IP   (Set in RoboDK program)
RoboDK_Port = 5000            # RoboDK Port (Set in RoboDK program)
Kuka_IP = '172.31.1.147'      # Robot IP    (Found in Teach Pendant)
Kuka_Port = 7000              # Robot Port  (Found in Teach Pendant)


# Creates the logic of the proxy server, uses a reader and writer object within python to send/receive data 
async def proxy(reader, writer):
    # Runs until no more data being recieved
    while True:
        # Await allows us to run the "reader" coroutine read(), letting us read up to the next 2048 bytes
        data = await reader.read(2048)
        decoded_data = data.decode()
        # If what we read actually has data in it i.e. it's not empty
        if not data.strip():
            break

        # If what we read has the word "Extrude(" signifiying it's meant for the Sammy board, do stuff
        if "Extrude(" in decoded_data:

            print(f"WE GOT THE JUICE BABY... \nNevermind we got this command: {decoded_data}")
            #Write to serial port 
            Serial_Port.write(decoded_data[decoded_data.find("(")+1:decoded_data.find(")")].encode())
        
        # Run the "writer" coroutine write(), attempts to send the data immeadiately, if it fails the data
        # is queued in an internal buffer until it can be sent
        writer.write(data)
        # A drain call acts as flow control, if the internal buffer is too large, it blocks the program from continuing
        # allowing the data to be sent and the buffer to decrease to a low level. If there's nothing to wait for, the
        # await call will complete instantly if there is nothing to wait for
        await writer.drain()

    # closes the writer connection as there's no more data to read
    writer.close()

#Responsible for making the connection between RoboDK and KUKA
async def Make_Connection(RoboDK_Reader, RoboDK_Writer):
    # Establish a network connection and return a pair of (reader, writer) objects
    # The returned reader and writer objects are instances of StreamReader and StreamWriter classes.
    # These classes contain methods to read and send data
    KUKA_Reader, KUKA_Writer = await asyncio.open_connection(Kuka_IP, Kuka_Port)
    # wait for the proxy routines to detect data
    await asyncio.wait([proxy(RoboDK_Reader, KUKA_Writer), proxy(KUKA_Reader, RoboDK_Writer)])

# Set up the event loop if there isn't one already (on startup), or get the current event loop
EventLoop = asyncio.get_event_loop()
# Start a socket server which will run when the connection is made between RoboDK and KUKA
# and to use the EventLoop as the servers loop to run through
MainLoop = asyncio.start_server(Make_Connection, RoboDK_IP, RoboDK_Port, loop=EventLoop)

# Run the event loop until the "Main Loop" has completed 
ProxyServer = EventLoop.run_until_complete(MainLoop)

try:
    # Runs the event loop forever, until a stop is called
    EventLoop.run_forever()
except KeyboardInterrupt:
    # If you press "Ctrl-C, or the DEL key while the proxy is running move on"
    pass
finally:
    # Close all Listening sockets on the Proxy
    ProxyServer.close()
    # Close Serial Port
    Serial_Port.close()
    # Waits until the above command has finished, then replaces the MainLoop with nothing
    EventLoop.run_until_complete(ProxyServer.wait_closed())
    # Closes the eventloop, terminating all communication
    EventLoop.close()