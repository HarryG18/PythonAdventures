import socket as soc
import struct
import binascii

s = soc.socket(soc.AF_INET, soc.SOCK_RAW)
print(soc.gethostname())
s.bind((soc.gethostname(), 7000))
while True:
    packet = s.recv(2048)
    ethernet_header = packet[0][0:14]
    eth_header = struct.unpack("!6s6s2s", ethernet_header)
    print("Destination MAC:" + binascii.hexlify(eth_header[0]) + " Source MAC:" + binascii.hexlify(eth_header[1]) + " Type:" + binascii.hexlify(eth_header[2]))
    ipheader = packet[0][14:34]
    ip_header = struct.unpack("!12s4s4s", ipheader)
    print( "Source IP:" + soc.inet_ntoa(ip_header[1]) + " Destination IP:" + soc.inet_ntoa(ip_header[2]))