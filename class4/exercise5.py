# Class 4 exercise 5
'''
Use Netmiko to enter into configuration mode on pynet-rtr2
Also use Netmiko to verify your state(
i.e. that you are currently in configuration mode).
'''
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

pynet1 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password}
pynet2 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 8022}
juniper_srx = {'device_type': 'juniper', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 9822}

pynet_rtr2 = ConnectHandler(**pynet2)
pynet_rtr2.config_mode()
prompt = pynet_rtr2.find_prompt()
print prompt
