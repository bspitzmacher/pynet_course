'''
Class Juniper Automation Exercise 1
Use Juniper's PyEZ library to make a connection to the Juniper SRX and to print out the device's facts.
'''

from jnpr.junos import Device
from pprint import pprint

a_device = Device(host='184.105.247.76', user='pyclass', password='88newclass')
a_device.open()

pprint(a_device.facts)
