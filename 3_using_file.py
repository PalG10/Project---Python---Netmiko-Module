from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '129.119.125.181',
    'username': 'admin',
    'password': 'cisco',
    'port': 22
}

connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable


# using file, sending the commands
print('sending commands from file..')
output = connection.send_config_from_file('ospf.txt')
print(output)


# connection.send_command('write memory')
print('Closing connection')
connection.disconnect()
