# Class 4 exercise 8
'''
Use Netmiko to change the logging buffer size (logging buffered <size>)
and to disable console logging (no logging console) from a file on both pynet-rtr1 and pynet-rtr2.
File name = config_file.txt
'''
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

pynet1 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password}
pynet2 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 8022}
juniper_srx = {'device_type': 'juniper', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 9822}

pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr2 = ConnectHandler(**pynet2)
outp = pynet_rtr1.send_command("show run | inc logging")
print "RTR1 - Before change:\n%s" %(outp)
outp = pynet_rtr2.send_command("show run | inc logging")
print "\nRTR2 - Before change:\n%s" %(outp)
pynet_rtr1.send_config_from_file(config_file='config_file.txt')
pynet_rtr2.send_config_from_file(config_file='config_file.txt')
outp = pynet_rtr1.send_command("show run | inc logging")
print "\nRTR1 - After change:\n%s" %(outp)
outp = pynet_rtr2.send_command("show run | inc logging")
print "\nRTR2 - After change:\n%s" %(outp)
