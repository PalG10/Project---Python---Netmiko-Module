
from netmiko import ConnectHandler

# to enable logging process
# https://github.com/ktbyers/netmiko/blob/develop/COMMON_ISSUES.md
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Define cisco_ information
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '129.119.125.181',
    'username': 'admin',
    'password': 'cisco',
    'port': 22,                         # optional, default 22
}


connection = ConnectHandler(**cisco_device)
output = connection.send_command('show version')
print(output)

# closing connection
print('Closing Connection..')
connection.disconnect()
