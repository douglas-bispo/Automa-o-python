import getpass
import telnetlib

HOST = "localhost"
user = input("Digito o seu Usuario: ")
password = getpass.getpass()

lista_routers = open ('multirouters')

for ip in lista_routers:
    ip = ip.strip()
    print('Configurando o roteador ' + (ip))
    HOST = ip
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"conf t\n")
    for interface_loopback in range (1,4):
        tn.write(b"interface loopback" + str(interface_loopback).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))





