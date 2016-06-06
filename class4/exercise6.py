# Class 4 exercise 6
'''
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
'''
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

pynet1 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password}
pynet2 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 8022}
juniper_srx = {'device_type': 'juniper', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 9822}

pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr2 = ConnectHandler(**pynet2)
srx = ConnectHandler(**juniper_srx)

outp = pynet_rtr1.send_command("show arp")
print "Cisco Rtr1:\n%s" % (outp)

outp = pynet_rtr2.send_command("show arp")
print "\nCisco Rtr2:\n%s" % (outp)

outp = srx.send_command("show arp")
print "\nJuniper SRX:%s" % (outp)
