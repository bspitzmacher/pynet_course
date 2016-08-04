'''
Class Juniper Automation Exercise 2
For each of the SRX's interfaces, display: the operational state, 
packets-in, and packets-out. You will probably want to use EthPortTable for 
this.
'''

from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.op.ethport import EthPortTable


a_device = Device(host='184.105.247.76', user='pyclass', password='88newclass')
a_device.open()

ports = EthPortTable(a_device)
ports.get()

for i in ports.keys():
    print '*' * 80
    print i
    for k,v in ports[i].items():
        print k, v
