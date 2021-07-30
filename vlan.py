
import getpass
import telnetlib

HOST = "192.168.66.112"
user = input("Digito o seu Usuario: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Sales\n")
tn.write(b"vlan 3\n")
tn.write(b"name Eng\n")
tn.write(b"vlan 4\n")
tn.write(b"name Prod\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))












