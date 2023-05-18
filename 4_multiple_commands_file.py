from netmiko import ConnectHandler

#opening a text file “device.txt” and reading it in a list
with open('devices.txt')as f:
    devices = f.read().splitlines()

#creating an empty list,containing a dictionary for each router
device_list = list()


# iterating each devices mentioned in the device.txt to create a list
for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'admin',
        'password': 'cisco',
        'port': 22
    }

    device_list.append(cisco_device)
print(device_list)


# iterating over device list.
for device in device_list:
    connection = ConnectHandler(**device)

    # entering the enable mode.
    print('Entering the enable mode...')
    connection.enable()

    # prompting the user for configuration file.
    file = input(
        f'Enter a configuration file (use a valid path) for {device["host"]}:')

    print(f'Running commands from file: {file} on device: {device["host"]}')
    output = connection.send_config_from_file(file)
    print(output)

    print(f'Closing connection to {cisco_device["host"]}')

    print('Closing connection')
    connection.disconnect()

    # separating devices.
    print('#' * 30)
