#!/bin/python3
import sys
import socket
from datetime import datetime as dt
import pyfiglet

pyfiglet.print_figlet(text="welcome to Jaswanth's port scanner",colors="RED")


a = input("Enter the target: ")
try:
    target = socket.gethostbyname(a)
except socket.gaierror:
    print("Incomplete arguments or please enter a complete website name")
    sys.exit()

print("-" * 50)
print(f"Target: {target}")
print("Start time: " + str(dt.now()))
print("-" * 50)

print("Press 1 for scanning specific ports")
print("Press 2 for scanning popular ports")
print("Press 3 for scanning specific range of ports")

choice = int(input("Enter your choice: "))

if choice == 1:
    ports = []
    open_ports = []
    n = int(input("Enter number of ports you want to scan: "))
    print("Enter the ports that you want to scan: ")

    for i in range(n):
        x = int(input())
        ports.append(x)
    print("Scanning started")
    try:
        for i in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, i))
            if result == 0:
                open_ports.append(i)
            s.close()
        b = len(open_ports)
        print(f"{b} port(s) are open")
        print("The following ports are open:")
        for i in open_ports:
            print(i)
        print("Scanning complete")
        pyfiglet.print_figlet(text="Happy Hacking", colors="BLUE")
        
    except KeyboardInterrupt:
        print("Error by keyboard")
        sys.exit()
    except socket.error:
        print("Problem in connection")
        sys.exit()

elif choice == 2:
    a = {80: "http", 443: "https", 23: "telnet", 53: "dns", 22: "ssh", 25: "smtp", 20: "ftp"}
    r = 0
    try:
        print("Result: ")
        for i, j in a.items():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(2)
            result = s.connect_ex((target, i))
            if result == 0:
                print(f"Port {i} is open and the respective protocol is {j}")
                r += 1
            s.close()
        print(f"Scanning completed for some popular ports and {r} port(s) are open")
        pyfiglet.print_figlet(text="Happy Hacking", colors="BLUE")
         
    except KeyboardInterrupt:
        print("Something interrupted by you")
        sys.exit()
    except socket.error:
        print("There is a problem in connection with the respective target")
        sys.exit()

elif choice == 3:
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))
    try:
        print("Scanning started")
        for i in range(start, end + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, i))
            if result == 0:
                print(i, "port is open")
            s.close()
        pyfiglet.print_figlet(text="Happy Hacking", colors="BLUE")
        
    except KeyboardInterrupt:
        print("Something interrupted by you")
        sys.exit()
    except socket.error:
        print("There is a problem in connection with the respective target")
        sys.exit()

