import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5000))
texttest = "HISHDAHSIDAHSDAD"
while True:
    msg = s.sendall(texttest.encode())
    