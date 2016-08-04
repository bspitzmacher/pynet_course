'''
Class Juniper Automation Exercise 3
Display the SRX's routing table. You will probably want to use RouteTable for this
(from jnpr.junos.op.routes import RouteTable).
'''

from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.op.ethport import EthPortTable
from jnpr.junos.op.routes import RouteTable

a_device = Device(host='184.105.247.76', user='pyclass', password='88newclass')
a_device.open()

routes = RouteTable(a_device)
routes.get()

for i in routes.keys():
    print '*' * 80
    print i
    for k,v in routes[i].items():
        print k, v
