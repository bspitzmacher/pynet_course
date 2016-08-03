'''
Class 8 Exercise 4
Remove the two objects created in the previous exercise from the database.
'''

from net_system.models import NetworkDevice, Credentials
import django

net_devices = NetworkDevice.objects.all()
django.setup()

for a_device in net_devices:
    if 'test' in a_device.device_name:
        a_device.delete()

# As requested, requery the DB to refresh 'net-devices'
net_devices = NetworkDevice.objects.all()

for a_device in net_devices:
    print a_device
