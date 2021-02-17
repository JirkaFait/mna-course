from netmiko import ConnectHandler
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
loger = logging.getLogger("netmiko")


def gen_tplink_connect_opt(host, port, password):
    tplink_t1600 = {
        'device_type': 'tplink_jetstream',
        'host': host,
        'username': 'admin',
        'password': password,
        'port': port,
        'verbose': True,
    }
    return tplink_t1600


con_str = gen_tplink_connect_opt('10.40.1.10', 22, 'piatkovinatojedrina')
connection = ConnectHandler(**con_str)

# getting the router's prompt
prompt = connection.find_prompt()
print(prompt)
if '>' in prompt:
    connection.enable()  # entering the enable mode

output = connection.send_command('show mac-vlan mac-address b4:f5:24:0a:93:ed')
print(output)

if not connection.check_config_mode():  # returns True if it's already in the global config mode
    connection.config_mode()  # entering the global config mode

print(connection.check_config_mode())
cmd = 'mac-vlan mac-address b4:f5:24:0a:93:ed vlan 5 description TECHNIK'
output = connection.send_command(cmd)
print(output)

# cmd = 'mac-vlan mac-address aa:bb:cc:dd:ee:ff vlan 3 description POKUS'
# output = connection.send_command(cmd)
# # output = connection.send_command('user name u6 password cisco')
# print(output)

connection.exit_config_mode()  # exiting the global config mode
print(connection.check_config_mode())
# yapiseme
output = connection.send_command('copy running-config startup-config')
print(output)

output = connection.send_command('show mac-vlan mac-address b4:f5:24:0a:93:ed')
print(output)

print('Closing connection')
connection.disconnect()
