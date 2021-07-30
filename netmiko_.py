from netmiko import ConnectHandler

R1 = {
   'device_type': 'cisco_ios',
   'host': '192.168.66.131',
   'username': 'douglas',
   'password': 'teste',
   }
connect = ConnectHandler(**R1)

loopback13 = ['interface loopback 13']

configurar = connect.send_config_set(loopback13)
output = connect.send_command("show ip int brief")

print(output)


