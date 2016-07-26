'''
Class 8 Exercise 4
Remove the two objects created in the previous exercise from the database.
'''

from net_system.models import NetworkDevice, Credentials

net_devices = NetworkDevice.objects.all()

for a_device in net_devices:
    if 'test' in a_device.device_name:
        a_device.delete()
        
for a_device in net_devices:
    print a_device
