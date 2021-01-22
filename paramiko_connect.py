import paramiko

# creating an ssh client object
ssh_client = paramiko.SSHClient()
print(type(ssh_client))
host = '192.168.10.252'
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('Connecting to {}'.format(host))
ssh_client.connect(hostname=host, port=22, username='admin', password='admin',
                   look_for_keys=False, allow_agent=False)


# checking if the connection is active
print(ssh_client.get_transport().is_active())

# sending commands
# ...

print('Closing connection')
ssh_client.close()