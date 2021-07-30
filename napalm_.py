from napalm import get_network_driver
import json

driver = get_network_driver("ios")

device = driver(
        hostname="192.168.66.131",
        username="douglas",
        password="teste",
        optional_args={"port": 22},
    )
device.open()

output = device.get_arp_table()
print(json.dumps(output, indent=4))

print('Configurando BGP no Router... Aguarde...')

device.load_merge_candidate(filename='r1config.cfg')
device.commit_config()
device.close()

#output = device.get_bgp_neighbors()
#print(json.dumps(output, indent=4))