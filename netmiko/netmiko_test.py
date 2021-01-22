from netmiko import ConnectHandler

tplink_t1600 = {
    'device_type': 'tplink_jetstream',
    'host':   '192.168.10.252',
    'username': 'admin',
    'password': 'piatkoUZneni',
    'port': 22,
    'verbose': True,
}

connection = ConnectHandler(**tplink_t1600)
output = connection.send_command('show mac-vlan all')

print(output)

# closing the connection
print('Closing connection')
connection.disconnect()