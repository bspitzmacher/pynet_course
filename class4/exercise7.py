# Class 4 exercise 7
'''
Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
'''
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

pynet1 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password}
pynet2 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 8022}
juniper_srx = {'device_type': 'juniper', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 9822}

pynet_rtr2 = ConnectHandler(**pynet2)
outp = pynet_rtr2.send_command("show run | inc logging")
print "Before change:\n%s" %(outp)
config_commands = ['logging buffered 20000']
outp = pynet_rtr2.send_config_set(config_commands)
outp = pynet_rtr2.send_command("show run | inc logging")
print "\nAfter change:\n%s" %(outp)
