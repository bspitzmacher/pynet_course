'''
Class Juniper Automation Exercise 4
Use the PyEZ load() method to set the hostname of the SRX using set, conf (curly brace), and XML formats.
After each load(), display the differences between the running config and the candidate config.
Additionally, perform at least one commit and one rollback(0) in this program.
The committed hostname at the end of the program should be:  pynet-jnpr-srx1
'''

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

a_device = Device(host='184.105.247.76', user='pyclass', password='88newclass')
a_device.open()

cfg = Config(a_device)

cfg.load("set system host-name foo", format="set", merge=True)
print "Hostname Change using 'set' format:"
print cfg.pdiff()
print "*" * 80
print "Rollback candidate config"
cfg.rollback(0)
print cfg.pdiff()
print "*" * 80

cfg.load(path="exercise4.conf", format="text", merge=True)
print "Hostname Change using 'text' format:"
print cfg.pdiff()
print "*" * 80
print "Committing hostname change."
cfg.commit(comment="Changing hostname to bar")

cfg.load(path="exercise4.xml", format="xml", merge=True)
print "Hostname Change using 'xml' format:"
print cfg.pdiff()
print "*" * 80

print "Committing hostname change"
cfg.commit(comment="Changing hostname back to pynet-jnpr-srx1")
