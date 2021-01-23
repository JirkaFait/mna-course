from netmiko import ConnectHandler
import logging
logging.basicConfig(filename='test.log', level=logging.INFO)
loger = logging.getLogger("netmiko")

tplink_t1600 = {
    'device_type': 'tplink_jetstream',
    'host': '192.168.10.252',
    'username': 'admin',
    'password': 'piatkoUZneni',
    'port': 22,
    'verbose': True,
}
connection = ConnectHandler(**tplink_t1600)

# getting the router's prompt
prompt = connection.find_prompt()
print(prompt)
if '>' in prompt:
     connection.enable()  # entering the enable mode

output = connection.send_command('show mac-vlan all')
print(output)

if not connection.check_config_mode():  # returns True if it's already in the global config mode
    connection.config_mode()  # entering the global config mode

print(connection.check_config_mode())
cmd = 'mac-vlan mac-address 00:1F:85:FB:63:35 vlan 4 description faitmac'
connection.send_command(cmd)
# output = connection.send_command('user name u6 password cisco')
print(output)

connection.exit_config_mode()  # exiting the global config mode
print(connection.check_config_mode())
# yapiseme

output = connection.send_command('copy running-config startup-config')
print(output)

output = connection.send_command('show mac-vlan all')
print(output)

print('Closing connection')
connection.disconnect()
