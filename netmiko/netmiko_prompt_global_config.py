from netmiko import ConnectHandler
tplink_t1600 = {
    'device_type': 'tplink_jetstream',
    'host':   '192.168.10.252',
    'username': 'admin',
    'password': 'admin',
    'port': 22,
    'verbose': True,
}
connection = ConnectHandler(**tplink_t1600)

# getting the router's prompt
prompt = connection.find_prompt()
# if '>' in prompt:
#        connection.enable(cmd='enable')   # entering the enable mode

output = connection.send_command('sh run')
print(output)

if not connection.check_config_mode(): # returns True if it's already in the global config mode
       connection.config_mode()  # entering the global config mode

# print(connection.check_config_mode())
connection.send_command('username u3 secret cisco')

connection.exit_config_mode()  # exiting the global config mode
print(connection.check_config_mode())

print('Closing connection')
connection.disconnect()