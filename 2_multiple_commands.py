from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': 'R1.txt',
    'username': 'admin',
    'password': 'cisco',
    'port': 22
}

connection = ConnectHandler(**cisco_device)


# checking the prompt, if user in user-exac mode change to priviledge mode
prompt = connection.find_prompt()
if '>' in prompt:
    print('Entering the enable mode...')
    connection.enable()


# checking the prompt, and switching to global configuration mode.
if not connection.check_config_mode():
    connection.config_mode()


commands = ['int loopback 0', 'ip address 3.3.3.3 255.255.255.255',
            'exit']

# displaying the commands
output = connection.send_config_set(commands)

# priting the output
print(output)


# exiting from global configuration mode
connection.exit_config_mode()


# saving and exiting the configuration
connection.send_command('write memory')
print('Closing connection')
connection.disconnect()
