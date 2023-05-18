from datetime import datetime
from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '129.119.125.181',
    'username': 'admin',
    'password': 'cisco',
    'port': 22,                         # optional, default 22
}


connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()


# getting the hostname from the device
output = connection.send_command('show run')
prompt = connection.find_prompt()
hostname = prompt[0:-1]

# getting currwent date and time
now = datetime.now()
year = now.year
month = now.month
day = now.day

# creating a file backup of the device configuration
# using hostname + current date
filename = f'{hostname}-{year}-{month}-{day}-backup.txt'
with open(filename, 'w') as backup:
    backup.write(output)
    print(f'Backup of {hostname} completed successfully.')


print('Closing connection')
connection.disconnect()
