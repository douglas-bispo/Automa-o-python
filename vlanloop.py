import getpass
import telnetlib

HOST = "192.168.66.131"
user = input("Digito o seu Usuario: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
tn.write(b"conf t\n")
for vlans in range (10,16):
    tn.write(b"Vlan " + str(vlans).encode('ascii') + b"\n")
    tn.write(b"name Site_ " + str(vlans).encode('ascii') + b"\n")
tn.write(b"end\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))





