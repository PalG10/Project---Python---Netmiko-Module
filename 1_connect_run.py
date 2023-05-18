from netmiko import ConnectHandler

# creating a dictionary with device specification
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '129.119.125.181',
    'username': 'admin',
    'password': 'cisco',
    'port': 22,                         # optional, default 22
}

# creating an SSH connection to the Cisco device
connection = ConnectHandler(**cisco_device)


# retrieving the running configuration
output = connection.send_command("sh run")
print(output)


# closing connection
print('Closing connection')
connection.disconnect()
