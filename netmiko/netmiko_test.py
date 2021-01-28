from netmiko import ConnectHandler
import logging
import time
logging.basicConfig(filename='test.log', level=logging.DEBUG)
loger = logging.getLogger("netmiko")

tplink_t1600 = {
    'device_type': 'tplink_jetstream',
    'host':   '192.168.10.252',
    'username': 'admin',
    'password': 'piatkovinatojedrina',
    'port': 22,
    'verbose': True,
}

connection = ConnectHandler(**tplink_t1600)
prompt = connection.find_prompt()
print(prompt)
if '>' in prompt:
     connection.enable()  # entering the enable mode


# print(connection.base_prompt)
time.sleep(3)
connection.clear_buffer()

output = connection.send_command(command_string='show mac-vlan all')

print(output)

# closing the connection
print('Closing connection')
connection.disconnect()